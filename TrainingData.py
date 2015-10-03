import urllib.request
import zipfile
import os
from subprocess import call

urls = {
	'7zip': 'http://www.7-zip.org/a/7za920.zip',
	'trainingData': 'http://www.cs.cmu.edu/afs/cs.cmu.edu/project/theo-8/faceimages/faces.tar.Z'

}


def download7Zip():
	filename = '7za.zip'
	
	# Download 7zip
	print("Download 7zip archive...")
	urllib.request.urlretrieve(urls['7zip'], filename)
	
	# Open as file
	fh = open(filename, 'rb')
	z = zipfile.ZipFile(fh)
	
	# Get 7zip exe file
	sevenZipFile = [x for x in z.namelist() if x.endswith("exe")][0]
	
	# Extract the exe file
	print("Extracting {0}".format(sevenZipFile))
	z.extract(sevenZipFile)
	
	fh.close()
	
	# Delete 7zip downloaded .zip container
	print("Cleaning up...")
	os.remove(filename)
	
def downloadTrainingData():
	filename = 'trainingData.tar.Z'
	
		
	print("Downloading training data...")
	# Download trainingdata
	urllib.request.urlretrieve(urls['trainingData'], filename)
		
	
	call(['7za.exe', 'x', 'trainingData.tar.Z', '-y'], stdout=open(os.devnull, 'wb'))
	print("Extracted from tar.Z: Complete")
	call(['7za.exe', 'x', 'trainingData.tar', '-y'], stdout=open(os.devnull, 'wb'))
	print("Extracted from tar: Complete")
	
	
	print("Cleaning up...")
	os.remove("trainingData.tar.Z")
	os.remove("trainingData.tar")
	print("Done!")


def cleanup():
	os.remove('7za.exe')
	
	
	
# Execute procedures
download7Zip()
downloadTrainingData()
cleanup()