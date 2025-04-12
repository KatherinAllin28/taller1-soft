# bring_u/simple_logger.py

import logging
import os
from django.conf import settings

class SimpleLogger:
    """
    Un logger simple para registrar acciones en la aplicación
    """
    
    def __init__(self):
        # Configurar el logger
        self.logger = logging.getLogger('bring_u_simple')
        self.logger.setLevel(logging.INFO)
        
        # Evitar que se registren duplicados
        if not self.logger.handlers:
            # Crear directorio de logs si no existe
            logs_dir = os.path.join(settings.BASE_DIR, 'logs')
            if not os.path.exists(logs_dir):
                os.makedirs(logs_dir)
            
            # Configurar el archivo de log
            file_handler = logging.FileHandler(os.path.join(logs_dir, 'bring_u.log'))
            file_handler.setLevel(logging.INFO)
            
            # Formato del log
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            
            # Añadir el manejador al logger
            self.logger.addHandler(file_handler)
    
    def info(self, message):
        """Registrar información general"""
        self.logger.info(message)
    
    def warning(self, message):
        """Registrar advertencias"""
        self.logger.warning(message)
    
    def error(self, message):
        """Registrar errores"""
        self.logger.error(message)
    
    def log_request(self, action, request_id, user_id=None):
        """Registrar acciones relacionadas con solicitudes"""
        user_info = f" por Usuario: {user_id}" if user_id else ""
        self.info(f"Solicitud {request_id}: {action}{user_info}")
    
    def log_delivery(self, action, delivery_id, request_id=None):
        """Registrar acciones relacionadas con entregas"""
        request_info = f" - Solicitud: {request_id}" if request_id else ""
        self.info(f"Entrega {delivery_id}: {action}{request_info}")
    
    def log_user(self, action, user_id):
        """Registrar acciones de usuario"""
        self.info(f"Usuario {user_id}: {action}")

# Crear una instancia singleton del logger
logger = SimpleLogger()