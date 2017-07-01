import os

# TODO: Remove code duplication. All the 'open', 'next' and 'write file' methods can be replaced by a single one.
#       Take a look in the Importer.py class to see how it can be done.


class ImporterPathway:

    def __init__(
            self,
            pathway_super_class_file=None,
            pathway_class_file=None,
            pathway_file=None,
            keggreader=None):

        self.pathway_super_class_file = pathway_super_class_file
        self.pathway_class_file = pathway_class_file
        self.pathway_file = pathway_file

        self.reader = keggreader

        self.pathway_super_class_primary_key = 0
        self.pathway_super_classes_inserted = {}

        self.pathway_class_primary_key = 0
        self.pathway_classes_inserted = {}

        self.pathway_name_primary_key = 0
        self.pathway_names_inserted = {}
        self.pathway_maps_inserted = {}

        self.purge_old_files(
            pathway_super_class_file,
            pathway_class_file,
            pathway_file)

    # TODO: test, comment
    def purge_old_files(
            self,
            pathway_super_class=None,
            pathway_class=None,
            pathway=None):

        if os.path.exists(pathway_super_class):
            os.remove(pathway_super_class)

        if os.path.exists(pathway_class):
            os.remove(pathway_class)

        if os.path.exists(pathway):
            os.remove(pathway)

    def next_pathway_super_class_primary_key(self):
        """
        Controls the pathways table primary key counter.

        Returns:
            (int): An integer representing the new primary key.

        """

        self.pathway_super_class_primary_key += 1

        return self.pathway_super_class_primary_key

    def next_pathway_class_primary_key(self):
        """
        Controls the pathways table primary key counter.

        Returns:
            (int): An integer representing the new primary key.

        """

        self.pathway_class_primary_key += 1

        return self.pathway_class_primary_key

    def next_pathway_name_primary_key(self):
        """
        Controls the pathways table primary key counter.

        Returns:
            (int): An integer representing the new primary key.

        """

        self.pathway_name_primary_key += 1

        return self.pathway_name_primary_key

    def write_pathway_super_classes_file(
            self,
            pathway_super_classes_file=None,
            pathway_super_class=None):
        """
        Actual write the pathways inserts file, log the operation and keep the inserted ids.
        """

        next_id = self.next_pathway_super_class_primary_key()

        pathway_super_classes_file.write(
            str(next_id) + '\t' + str(pathway_super_class) + "\n")

        self.pathway_super_classes_inserted[str(pathway_super_class)] = next_id

    def write_pathway_classes_file(
            self,
            pathway_classes_file=None,
            pathway_super_class_id=None,
            pathway_class=None):
        """
        Actual write the pathways inserts file, log the operation and keep the inserted ids.
        """

        next_id = self.next_pathway_class_primary_key()

        pathway_classes_file.write(
            str(next_id) +
            '\t' +
            str(pathway_super_class_id) +
            '\t' +
            str(pathway_class) +
            "\n")

        self.pathway_classes_inserted[str(pathway_class)] = next_id

    def write_pathway_names_file(
            self,
            pathway_names_file=None,
            pathway_class_id=None,
            pathway_map=None,
            pathway_name=None):
        """
        Actual write the pathways inserts file, log the operation and keep the inserted ids.
        """

        next_id = self.next_pathway_name_primary_key()

        pathway_names_file.write(
            str(next_id) +
            '\t' +
            str(pathway_class_id) +
            '\t' +
            str(pathway_map) +
            '\t' +
            str(pathway_name) +
            "\n")

        self.pathway_names_inserted[str(pathway_name)] = next_id
        self.pathway_maps_inserted[str(pathway_map)] = next_id

    def write_pathways(self):
        """
        Write the pathways insert file.
        """

        pathways_destination = open(self.pathway_super_class_file, 'a')
        pathways_class_destination = open(self.pathway_class_file, 'a')
        pathways_names_destination = open(self.pathway_file, 'a')

        pathways = self.reader.getAllPathways()

        # Pathway super class
        for pathway_super_class, pathway_data in pathways.iteritems():
            self.write_pathway_super_classes_file(
                pathways_destination, pathway_super_class)

            # Pathway class
            for pathway_class, data in pathway_data.iteritems():
                self.write_pathway_classes_file(
                    pathways_class_destination,
                    self.pathway_super_classes_inserted[pathway_super_class],
                    pathway_class)

                # Pathway map and name
                for pathway_map, pathway_name in data.iteritems():
                    self.write_pathway_names_file(
                        pathways_names_destination,
                        self.pathway_classes_inserted[pathway_class],
                        pathway_map,
                        pathway_name)

        pathways_destination.close()
        pathways_class_destination.close()
        pathways_names_destination.close()
