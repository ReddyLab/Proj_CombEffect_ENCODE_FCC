
###
REGION_GATA1_HDAC6 = [
    "chrX:48,750,000-48,850,000", ### CRISPRi-HCRFF (Zoom in)
    "chrX:48,397,930-49,656,988", ### CRISPRi-HCRFF (Screen)
    "chrX:48,000,000-49,500,000", ### CRISPRi-E2G
]

REGION_MYC_PVT1 = [
    "chr8:127,530,000-128,150,000", ### CRISPRi-HCRFF (Zoom in)
    "chr8:126,736,094-128,735,225", ### CRISPRi-HCRFF (Screen)
    "chr8:127,000,000-130,000,000", ### CRISPRi-E2G
]

REGION_FADS_FEN = [
    "chr11:61,788,000-61,897,000", ### CRISPRi-HCRFF (Zoom in)
    "chr11:61,788,524-61,897,153", ### CRISPRi-HCRFF (Screen)
    "chr11:61,777,000-61,993,000", ### CRISPRi-E2G
]

REGION_LMO2_CAPRIN1_CAT = [
    "chr11:33,700,000-34,497,000", ### CRISPRi-HCRFF (Zoom in)
    "chr11:33,064,196-34,664,117", ### CRISPRi-HCRFF (Screen)
    "chr11:33,826,000-34,930,000", ### CRISPRi-E2G
]

REGION_HBE_HBG = [
    "chr11:5,130,000-5,550,000", ### CRISPRi-HCRFF (Zoom in)
    "chr11:4,091,884-6,419,310", ### CRISPRi-HCRFF (Screen)
    "chr11:5,130,000-5,550,000", ### CRISPRi-E2G
]

REGION_MYB_HBS1L = [
    "chr6:134,850,000-135,450,000", ### CRISPRi-HCRFF (Zoom in)
    "chr6:134,253,831-136,927,585", ### CRISPRi-HCRFF (Screen)
    "chr6:123,601,000-144,991,500", ### CRISPRi-E2G
]




###
DCT_REGION = dict()

DCT_REGION["GATA1"] = REGION_GATA1_HDAC6
DCT_REGION["MYC"]   = REGION_MYC_PVT1
DCT_REGION["FADS"]  = REGION_FADS_FEN
DCT_REGION["HBE"]   = REGION_HBE_HBG
DCT_REGION["LMO2"]  = REGION_LMO2_CAPRIN1_CAT
DCT_REGION["MYB"]   = REGION_MYB_HBS1L

###
DCT_GENE = dict()

DCT_GENE["GATA1"] = ["GATA1", "HDAC6"]
DCT_GENE["MYC"]   = ["MYC",   "PVT1"]
DCT_GENE["FADS"]  = ["FADS1", "FADS2", "FADS3", "FEN1"]
DCT_GENE["HBE"]   = ["HBG1",  "HBG2",  "HBE1"]
DCT_GENE["LMO2"]  = ["LMO2", "CAPRIN1", "CAT"]
DCT_GENE["MYB"]   = ["HBS1L",   "MYB"]

###
DCT_GENE_FULL = dict()

DCT_GENE_FULL["GATA1"] = ["GATA1", "HDAC6"]
DCT_GENE_FULL["MYC"]   = ["MYC",   "PVT1"]
DCT_GENE_FULL["FADS"]  = ["FADS1", "FADS2", "FADS3", "FEN1"]
DCT_GENE_FULL["HBE"]   = ["HBG1",  "HBG2",  "HBE1"]
DCT_GENE_FULL["LMO2"]  = ["LMO2", "CAPRIN1", "CAT"]
DCT_GENE_FULL["MYB"]   = ["HBS1L",   "MYB"]