from BeautifulSoup import BeautifulStoneSoup

class XMLParser(object):

	def __init__(self):
		pass
	def SetXML(self,file):

		self.xml = file
		self.soup = BeautifulStoneSoup(xml)
		self.xmlParsed = {}
	
	def FieldsToParse(self,fields):
		self.fields = fields

	def Parse(self):

		for field in self.fields:
			
			items = self.soup.findAll(field)
			for item in items:
				for child in item.findChildren():
					
					try:
						
						self.xmlParsed[str(child.name)].append(str(child.text))

					except:
						
						self.xmlParsed[str(child.name)] = []
						self.xmlParsed[str(child.name)].append(str(child.text))

	def GetXML(self):
		return self.xmlParsed



class CreateCSV(object):
	def __init__(self,fileName):
		self.fileName = fileName
		self.file = open(fileName,'w')
	def WriteCSV(self,hora,minuto,dictionary):
		#string = str(hora) +'#'+ str(minuto) + '#' + str(dictionary[vehicle])
		#self.file.writelines()
		if (len(dictionary['vehicle']) == len(dictionary['speed'])):
			if (len(dictionary['vehicle']) == len(dictionary['dynamap'])):
				for count in range(len(dictionary['vehicle'])):
					dados = {'hora': hora, 'minuto': minuto, 'vehicle' : dictionary['vehicle'][count],'speed' : dictionary['speed'][count], 'dynamap' : dictionary['dynamap'][count]}

					linha = '{hora};{minuto};{vehicle};{dynamap};{speed}\n'.format(**dados)
					#print linha
					self.file.writelines(linha)

	def CloseCSV(self):
		self.file.close()

if __name__=='__main__':

	import os
	import gzip
	xmlParser = XMLParser()
	csv = CreateCSV('CCr.csv')
	xmlParser.FieldsToParse(['smreport'])


	print os.path.abspath(__file__)
	for dirname, dirnames, filenames in os.walk('/Users/caio/Desktop/CCr'):
	    for filename in filenames:
	    	files =  os.path.join(dirname,filename)
	    	if files.split('.')[-1] == 'gz':
		    	xml = gzip.open(os.path.join(dirname,filename))
	        	xmlParser.SetXML(xml)
	        	xmlParser.Parse()
	        	hora,minuto = dirname.split('/')[-2],dirname.split('/')[-1]
	        	print hora,minuto
	        	print dirname.split('/')
	        	csv.WriteCSV(hora,minuto,xmlParser.GetXML())

	csv.CloseCSV()