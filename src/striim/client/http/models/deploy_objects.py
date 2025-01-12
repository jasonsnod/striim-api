class FlowDeploy:

    def __init__(self, flow_name, servers_specification, deployment_group):

        if not flow_name:
            raise Exception('The FlowDeploy object must have a name for the floow being described in the deployment.')
        
        self.__flow_name = flow_name
        self.__servers_specification = servers_specification if servers_specification else 'default'
        self.__deployment_group = deployment_group if deployment_group else 'default'

        self.set_flow_deploy_command()
        print(f'FlowDeploy object instantiated for {flow_name}')

    def set_flow_deploy_command(self):
        
        flow_servers_specification_arg = f'on {self.__servers_specification} ' if self.__servers_specification.lower() != 'default' else ''
        flow_deployment_group_arg = f'in {self.__deployment_group} ' if self.__deployment_group.lower() != 'default' else ''
        
        self.__flow_deploy_command = f'with {self.__flow_name} {flow_servers_specification_arg} {flow_deployment_group_arg}'

    def get_flow_deploy_command(self):

        return self.__flow_deploy_command



class AppDeploy():

    __flow_deploy_objects = []

    def __init__(self, application_name, servers_specification, deployment_group, *flow_deployment_groups):

        if not application_name:
            raise Exception('The AppDeploy object must have an application name included to describe which app to deploy.')
        
        self.__application_name = application_name
        self.__servers_specifications = servers_specification if servers_specification else 'default'
        self.__deployment_group = deployment_group if deployment_group else 'default'

        if flow_deployment_groups:
            for flow in flow_deployment_groups:

                if isinstance(flow, FlowDeploy):
                    self.__flow_deploy_objects.append(flow)

        self.set_app_deploy_command()
        print(f'AppDeploy object instantiated for {application_name}')

    def set_app_deploy_command(self):
        app_servers_specification_arg = f'on {self.__servers_specification} ' if self.__servers_specification.lower() != 'default' else ''
        app_deployment_group__arg = f'in {self.__deployment_group} ' if self.__deployment_group.lower() != 'default' else ''

        app_deploy_command = f'{self.__application_name} {app_servers_specification_arg} {app_deployment_group__arg} '

        for flow in self.__flow_deploy_objects:
            app_deploy_command += flow.get_flow_depploy_command()

        self.__app_deploy_command = app_deploy_command

    def get_app_deploy_command(self):

        return f'DEPLOY APPLICATION {self.__app_deploy_command};'

    
        


        

        