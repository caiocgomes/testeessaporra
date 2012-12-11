from BeautifulSoup import BeautifulStoneSoup

class XMLParser(object):

	def __init__(self):
		pass
	def SetXML(self,file):

		self.xml = file
		self.soup = BeautifulStoneSoup(self.xml)
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

import sys
try:
	xmlParser = XMLParser()
	xmlParser.FieldsToParse(['smreport'])
	for text in sys.stdin:
		textI = text.strip().split('\t')
		

		xml,year,month,day,hour,minute = textI

		xmlParser.SetXML(xml)
		xmlParser.Parse()

		dictionary = xmlParser.GetXML()

		if (len(dictionary['vehicle']) == len(dictionary['speed'])):
			if (len(dictionary['vehicle']) == len(dictionary['dynamap'])):
				for count in range(0,len(dictionary['vehicle'])):
					dados = {'vehicle' : dictionary['vehicle'][count],'speed' : dictionary['speed'][count], 'dynamap' : dictionary['dynamap'][count],'year':year,'month':month,'day':day,'hour':hour,'minute':minute}


					linha = '{dynamap}\t{vehicle}\t{speed}\t{year}\t{month}\t{day}\t{hour}\t{minute}'.format(**dados)
					print linha
					

except:
	pass