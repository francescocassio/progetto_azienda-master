crea_tabella_videogiochi = """CREATE TABLE videogiochi(
	Rank INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Platform VARCHAR(50),
    Year_v YEAR,
    Genre VARCHAR(50),
    Publisher VARCHAR(50),
    NA_Sales DECIMAL(7,2),
    EU_Sales DECIMAL(7,2),
    JP_Sales DECIMAL(7,2),
    Other_Sales DECIMAL(7,2),
    Global_Sales DECIMAL(7,2),
    UNIQUE(Name, Platform, Year_v)
);"""