import os


class ImporterOrganism:

    def __init__(self, destination_file=None, keggreader=None):

        self.destination_file = destination_file

        self.organism_primary_key = 0
        self.organisms_inserted = {}

        self.reader = keggreader

        self.purge_old_file(self.destination_file)

    # TODO: test, comment
    def purge_old_file(self, destination_file=None):

        if os.path.exists(destination_file):
            os.remove(destination_file)

    def next_organism_primary_key(self):
        """
        Controls the organisms table primary key counter.

        Returns:
            (int): An integer representing the new primary key.

        """

        self.organism_primary_key += 1

        return self.organism_primary_key

    def write_organisms_file(
            self,
            organism_file=None,
            organism_code=None,
            organism_kegg_name=None,
            organism_internal_kegg_id=None,
            taxonomy_id=None):
        """
        Actual write the organisms inserts file, log the operation and keep the inserted ids.
        """

        next_id = self.next_organism_primary_key()

        organism_file.write(
            str(next_id) +
            '\t' +
            str(organism_code) +
            '\t' +
            str(organism_kegg_name) +
            '\t' +
            str(organism_internal_kegg_id) +
            '\t' +
            str(taxonomy_id) +
            "\n")

        self.organisms_inserted[str(organism_code)] = next_id

    def write_organisms(self):
        """
        Write the organisms insert file.
        """

        organisms = self.reader.getAllOrganisms()

        with open(self.destination_file, 'a') as f:

            for organism_code, organism_data in organisms.iteritems():
                self.write_organisms_file(
                    f,
                    organism_code,
                    organism_data['genome']['kegg_definition_name'],
                    organism_data['genome']['kegg_organism_id'],
                    organism_data['genome']['taxonomy_id'])
