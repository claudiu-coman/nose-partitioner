from nose.plugins import Plugin
from nose.selector import Selector


class PartitionSelector(Selector):
    def __init__(self, config, partition_count, partition):
        super(PartitionSelector, self).__init__(config)

        self.partition_count = partition_count
        self.partition = partition

    def wantFile(self, filename):
        """Hashing the file name should provide enough random dispersion. """
        if hash(filename) % self.partition_count == self.partition:
            return super(PartitionSelector, self).wantFile(filename)
        return False


class Partitioner(Plugin):
    """Split tests into several partitions, based on a deterministic hashing
    algorithm applied at file level. You will then be able to run nose over
    a selected partition provided as input.
    """
    enabled = True
    partition_count = 0
    partition = 0

    def options(self, parser, env):
        """
        Add options to command line.
        """
        super(Partitioner, self).options(parser, env)

        parser.add_option('--partitioner-num-partitions', action='store',
                          dest='partition_count',
                          default=None,
                          help='Number of partitions the test collection '
                               'will be split into')
        parser.add_option('--partitioner-partition', action='store',
                          dest='partition',
                          help='Partition to run tests from')

    def configure(self, options, conf):
        if not (options.partition_count and options.partition):
            self.enabled = False
            return

        self.partition_count = int(options.partition_count)
        self.partition = int(options.partition)

    def prepareTestLoader(self, loader):
        loader.selector = PartitionSelector(loader.config, self.partition_count, self.partition)
