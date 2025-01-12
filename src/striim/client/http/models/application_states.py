from enum import enum

class AppStates(Enum):
    
    APPROVING_QUIESCE = 'approving quiesce'
    COMPLETED = 'completed'
    CREATED = 'created'
    DEPLOY_FAILED = 'deploy failed'
    DEPLOYED = 'deployed'
    DEPLOYING = 'deploying'
    FLUSHING = 'flushing'
    HALT = 'halt'
    NOT_ENOUGH_SERVERS = 'not enough servers'
    QUIESCED = 'quiesced'
    QUIESCING = 'quiescing'
    RECOVERING_SOURCES = 'recovering sources'
    RUNNING = 'running'
    STARTING = 'starting'
    STARTING_SOURCES = 'starting sources'
    STOPPED = 'stopped'
    STOPPING = 'stopping'
    TERMINATED = 'terminated'
    UNKNOWN = 'unknown'
    VERIFYING_STARTING = 'verifying starting'