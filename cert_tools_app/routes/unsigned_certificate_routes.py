import io
import csv
import json
import pandas as pd

from flask import Blueprint, request, jsonify
from cert_tools.instantiate_v2_certificate_batch import create_unsigned_certificates_from_roster

unsigned_certificate_bp = Blueprint('unsigned_certificate_bp', __name__)

@unsigned_certificate_bp.route('/', methods=['POST'])
def create_unsigned_certificate():
    # Plantilla que se usará para crear los certificados sin firmar
    template_file = request.files['template']
    template = json.loads(template_file.read())
        
    # Archivo .csv de personas que recibirán un certificado
    roster = request.files['roster']
    
    if roster and roster.filename.endswith('csv'):
        try:
            df = pd.read_csv(roster)
            
            data_dict = df.to_dict(orient='records')
            
            return jsonify({"message": "File processed successfully", "data": data_dict}), 200
        
        except Exception as e:
            return jsonify({"error": str(e)}), 500