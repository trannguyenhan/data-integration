from engine.engine import EngineInterface
import xml.etree.ElementTree as ET
import utils.warehouse

class EngineXml(EngineInterface): 

    def extract_header(self):
        self.load_data_source()
        xml_tree = ET.parse(self.file)
        root = xml_tree.getroot()
        one_elements = root[0]
        
        for element in one_elements: 
            tag = element.tag
            value = element.text

            self.header.append(tag)
            self.data_sample[tag] = value

        self.file.close()
        return self.header

    def dump_data_to_warehouse(self, header_target, proj_name):
        self.extract_header()
        if len(self.header) != len(header_target): # (1)
            # schema source not fit with schema destination
            return False

        # load again data source
        result = []
        self.load_data_source()
        if self.file != None:
            xml_tree = ET.parse(self.file)
            root = xml_tree.getroot()

            for elements in root: 
                resultItem = {}
                cnt = 0
                
                for element in elements: 
                    tag = element.tag
                    value = element.text
                    resultItem[tag] = value
                    cnt += 1

                result.append(resultItem)
            
            utils.warehouse.dump(result, proj_name)
            return True

        return False


if __name__ == "__main__": 
    engine = EngineXml("/home/trannguyenhan/dataset/ign.csv", True)
    schema = engine.extract_schema()
    print(schema)