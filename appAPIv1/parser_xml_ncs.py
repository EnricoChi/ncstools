import os
import gzip
import zipfile

from lxml import etree


class ParseXML:
    """
    Parse data form XML file, can take zip or gzip
    Arguments:
        xml_file - str; string path to file gz or xml
        find_tag - str; default '{configData.xsd}configData'
    retrun data - dict 
    """
    def __init__(self, xml_file: str, find_tag: str ='{configData.xsd}configData') -> dict:
        self.file_opener = {
            'zip': self._open_zip,
            'gz': self._open_gz,
            'xml': self._open_xml,
        }
        self.xml_file = self._check_file(xml_file)
        self.file_type = self._get_file_type()
        self.find_tag = find_tag

    def __call__(self) -> dict:
        data = {}
        file = self.file_opener[self.file_type]()
        for _, element in etree.iterparse(file):
            if element.tag == self.find_tag:
                for elem in element.getchildren():
                    key = elem.attrib.get('id', 'Undefined')
                    data[key] = {el.attrib.get('id', 'Undefined'):
                        [e.attrib.get('id') for e in el.getchildren()]
                        for el in elem.getchildren()
                    }
        file.close()
        return data
    
    def _check_file(self, xml_file):
        if os.path.exists(xml_file):
            return xml_file
        raise FileNotFoundError(f'No file on {xml_file}')


    def _get_file_type(self) -> str:
        ft = self.xml_file.split('.')[-1]
        if ft not in self.file_opener.keys():
            raise ValueError('Unknow file format')
        return ft

    def _open_zip(self) -> 'file-like object':
        if zipfile.is_zipfile(self.xml_file):
            file = zipfile.ZipFile(self.xml_file)
            name = file.namelist()[0]
            return file.open(name, mode='r', pwd=None)
        raise ValueError('This is not zip file!')

    def _open_gz(self) -> 'file-like object':
        return gzip.open(self.xml_file, 'rb')

    def _open_xml(self) -> 'file-like object':
        return open(self.xml_file, 'rb')


if __name__ == "__main__":
    path_gz = 'sourcedata/source3g.xml.gz'
    path_xml = 'sourcedata/source3g.xml'
    path_zip = 'sourcedata/source3g.zip'
    if not os.path.exists(path_gz):
        exit('Test data not found!')
    
    parsexml_gz = ParseXML(path_gz)
    parsexml_xml = ParseXML(path_xml)
    parsexml_zip = ParseXML(path_zip)

    assert parsexml_gz() == {'ONRM_ROOT_MO_R': 
                            {'RNCE-EKT107':[
                                'EK0255-B',
                                'EK2058-B',
                                'EK3012',
                                'EK3013',
                                'RNCE-EKT107'],
                            'eNodeB_EKT': ['EK0019-B', 'EK0120-B']
                            }
                        }
    assert parsexml_xml() == {'ONRM_ROOT_MO_R': 
                            {'RNCE-EKT107':[
                                'EK0255-B',
                                'EK2058-B',
                                'EK3012',
                                'EK3013',
                                'RNCE-EKT107'],
                            'eNodeB_EKT': ['EK0019-B', 'EK0120-B']
                            }
                        }
    assert parsexml_zip() == {'ONRM_ROOT_MO_R': 
                            {'RNCE-EKT107':[
                                'EK0255-B',
                                'EK2058-B',
                                'EK3012',
                                'EK3013',
                                'RNCE-EKT107'],
                            'eNodeB_EKT': ['EK0019-B', 'EK0120-B']
                            }
                        }
    print('Test data from:')
    print(path_gz, path_xml, path_zip, sep='\n')
    print('Succesfuly!')

