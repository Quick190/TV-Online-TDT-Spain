static_icons = (('La 1', 'rtve.png'),
				('La 2', None),
				 ('Antena 3', 'antena3.png'),
				 ('La Sexta', 'a3media.png'),
				 ('A3Series', 'a3media.png'),
				 ('Nova', 'a3media.png'),
				 ('Neox', 'a3media.png'),
				 ('Mega', 'a3media.png'),
				 ('Real Madrid TV', None),
				 ('24h', None),
				 ('Teledeporte', None),
				 ('TVE 60 aniversario', None),
				 ('13TV', None),
				 ('DKiss', None),
				 ('Aragon TV - Aragon (AR)', 'aragontv.png'),
				 ('TPA - Asturias (AS)', None),
				 ('IB3 - Baleares (IB)', 'ib3.png'),
				 ('RTVC net - Canarias (CN)', None),
				 ('Popular TV - Cantabria (CB)', None),
				 ('TV3 - Catalu\xc3\xb1a (CT)', 'tv3.png'),
				 ('324 - Catalu\xc3\xb1a (CT)', None),
				 ('C33 - Catalu\xc3\xb1a (CT)', None),
				 ('8TV - Catalu\xc3\xb1a (CT)', None),
				 ('C. Extremadura - Extramadura (EX)', None),
				 ('Telemadrid - Madrid (MD)', 'telemadrid.png'),
				 ('Canal Parlamento - Madrid (MD)', None),
				 ('Navarra TV - Navarra (NC)', None),
				 ('Vaughan TV - Navarra (NC)', None),
				 ('Eitb - P.Vasco (PV)', None),
				 ('RTV Ceuta - Ceuta (CE)', None),
				 ('Ceuta TV - Ceuta (CE)', None),
				 ('Onda Algeciras TV - C\xc3\xa1diz (AN)', None),
				 ('TV Ibiza-Formentera - Baleares(IB)', None),
				 ('Popular TV - Cantabria (CB)', None),
				 ('Diocesano TV - Toledo (CM)', None),
				 ('BTV/Betev\xc3\xa9 - Barcerlona (CT)', None),
				 ('VOTV - Barcelona (CT)', None),
				 ('Andorra TV - Lleida (CT)', None),
				 ('Ribera TV - Valencia (VC)', None),
				 ('Sevilla F.C.', None),
				 ('Cordoba Internacional', 'CordobaInternacional.png'),
				 ('HispanTV', 'hispantv.png'))

def getIcon(channelName, method='static'):
	if method == 'static':
		for channel in static_icons:
			if channel[0] == channelName:
				return channel[1]
	else:
		return None

if __name__ == "__main__":
	print(getIcon('Cordoba Internacional'))
	print(getIcon('Sevilla F.C.'))
	print(getIcon('Vallmoll TV'))
