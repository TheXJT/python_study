DIAL_CODES=[(86,'China'),
	(91,'India'),
	(1,'United States'),
	(62,'Indonesia'),
	(55,'Brazil'),
	(92,'Pakistan'),
	(880,'Bangladesh'),
	(234,'Nigeria'),
	(7,'Russia'),
	(81,'japan'),]

country_code={country:code for code,country in DIAL_CODES}
country_code2={code:country.upper() for country,code in country_code.items() if code<66}
print(country_code2)