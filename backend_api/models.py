from sqlalchemy import Column, Integer, String, Float
from database import Base

class OCRHistory(Base):
    __tablename__ = "ocr_history"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    extracted_text = Column(String)
    confidence = Column(Float)