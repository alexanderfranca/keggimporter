import pprint
import os
import sys


class ImporterEc:

    def __init__(self, destination_file=None, keggreader=None):

        self.destination_file = destination_file

        self.ec_primary_key = 0
        self.ecs_inserted = {}

        self.reader = keggreader

        self.purge_old_file(destination_file)

    # TODO: test, comment
    def purge_old_file(self, destination_file=None):

        if os.path.exists(destination_file):
            os.remove(destination_file)

    def next_ec_primary_key(self):
        """
        Controls the ecs table primary key counter.

        Returns:
            (int): An integer representing the new primary key.

        """

        self.ec_primary_key += 1

        return self.ec_primary_key

    def write_ecs_file(self, ec_file=None, ec=None):
        """
        Actual write the ecs inserts file, log the operation and keep the inserted ids.
        """

        next_id = self.next_ec_primary_key()

        ec_file.write(str(next_id) + '\t' + str(ec) + "\n")

        self.ecs_inserted[str(ec)] = next_id

    def write_ecs(self):
        """
        Write the ecs insert file.
        """

        ecs = self.reader.getAllEcNumbers()

        with open(self.destination_file, 'a') as f:
            for ec in ecs:
                self.write_ecs_file(f, ec)
