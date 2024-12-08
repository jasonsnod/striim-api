import requests
from striim.client.http.api.striim

class TungstenConsole:

    TUNGSTEN_PATH = "/api/v2/tungsten"

    def __init__(self, striim_api_seesion):
        self.__striim_api_session = striim_api_seesion
        self.__tungsten_console_url = self.__striim_api_session.get_base_url

    
    def use_tql_file(self, tql_file_path=None):
        if tql_file_path:
            self.__striim_api_session.post()
    
    def deploy_app():
        return
    
    def describe_app():
        return
    
    def export_app():
        return
    
    def list_history_of_commands():
        return
    
    def import_app():
        return
    
    def list_objects():
        return
    
    def load_resource():
        return
    
    def meter_striim():
        return
    
    def monitor_component():
        return
    
    def preview_cq():
        return
    
    def quiesce_app():
        return
    
    def report_app():
        return
    
    def resume_app():
        return
    
    def select_wactionstore():
        return
    
    def show_curren_app_stream():
        return
    
    def start_app():
        return
    
    def status_of_app():
        return
    
    def stop_app():
        return

    def undeploy_app():
        return
    
    def unload_resource():
        return
    
    def usage_of_sources():
        return
    
