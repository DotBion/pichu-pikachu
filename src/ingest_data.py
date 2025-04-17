#implemetn factory design pattern
#have data coming in - identify the format of data coming in and ingest it
#factory can ingest several data formats

import zipfile

#defining an abstract class for data ingestor
class DataIngestor(ABC):
  @abstract method
  def ingest(self, file_path: str) -> pd.DataFrame:
    "Abstract method to ingest data from a given file"
    pass


#implementing a concrete class for ZIP Ingestion
class ZipDataIngestor(DataIngestor) :
  def ingest(self, file_path: str) -> pd.DataFrame :
    #ensuring file is a zip file
    if not file_path.endswith('.zip'):
      raise ValueError("The provided file is not a .zip file.")

    #extracting the zip file contents to a diff location
    with zipfile.ZipFile(file_path, "r") as zip_ref:
      zip_ref.extractall("extracted_data")

    #find the extracted csv file
    extracted_files = os.listdir("extracted_data")
    csv_files = [f for f in extracted_files if f.endswith(".csv")]

    if len(csv_files) == 0 :
      raise ValueError("No csv file found in the extracted daata")
    if len(csv_files) >= 1 :
      raise ValueError("moer than one csv files found")

    #read the csv file into data frame
    csv_file_path = os.path.join("extracted_data", csv_files[0])\
    df = pd.read_csv(csv_file_path)

    return df


#implementing a facotry to create DataIngestors

class DataIngestorFactory:
  @staticmethod
  def get_data_ingestor(file_extension: str) -> DataIngestor:
    #returns the apt ingestor based on filetype
    if file_extension == ".zip":
      return ZipDataIngestor()
    else :
      raise ValueError(f"No ingestor available for file extension : {file_extension}")

#example usage:

if __name__ == "__main__" :
  #filepath = 

  #determine file extension

  #get appropriate data ingesotor

  #ingest the data and load it into dataframes

  #pront head of df
  pass
