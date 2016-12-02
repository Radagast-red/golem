class Environment(object):

    opts                    = 'env.opts'
    opt                     = 'env.opt'
    opt_update              = 'env.opt.update'

    datadir                 = 'env.datadir'


class Crypto(object):

    pub_key                 = 'crypto.keys.pub'
    difficulty              = 'crypto.difficulty'


class Network(object):

    ident                   = 'net.ident'
    ident_key               = 'net.ident.key'

    peers_known             = 'net.peers.known'
    peers_connected         = 'net.peers.connected'

    peer                    = 'net.peer'
    peer_connect            = 'net.peer.connect'
    peer_disconnect         = 'net.peer.disconnect'

    supernodes              = 'net.supernodes'
    supernode               = 'net.supernode'
    supernode_create        = 'net.supernode.create'
    supernode_delete        = 'net.supernode.delete'

    p2p_port                = 'net.p2p.port'
    tasks_port              = 'net.tasks.port'

    evt_peer_connected      = 'evt.net.peer.connected'
    evt_peer_disconnected   = 'evt.net.peer.disconnected'
    evt_connection          = 'evt.net.connection'


class Reputation(object):

    computing               = 'rep.comp'
    requesting              = 'rep.requesting'
    evt_peer                = 'evt.rep.peer'


class Task(object):

    tasks                   = 'comp.tasks'
    tasks_check             = 'comp.tasks.check'
    tasks_stats             = 'comp.tasks.stats'
    tasks_known             = 'comp.tasks.known'
    tasks_known_delete      = 'comp.tasks.known.delete'

    task                    = 'comp.task'
    task_create             = 'comp.task.create'
    task_delete             = 'comp.task.delete'
    task_abort              = 'comp.task.abort'
    task_restart            = 'comp.task.restart'
    task_pause              = 'comp.task.pause'
    task_resume             = 'comp.task.resume'
    # task_price              = 'comp.task.price'
    # task_price_update       = 'comp.task.price.update'

    subtasks                = 'comp.task.subtasks'
    subtask                 = 'comp.task.subtask'
    subtask_restart         = 'comp.task.subtask.restart'

    evt_task_status         = 'evt.comp.task.status'
    evt_subtask_status      = 'evt.comp.subtask.status'


class Resources(object):

    dirs                    = 'res.dirs'
    dir_sizes               = 'res.dirs.sizes'

    evt_limit_exceeded      = 'evt.res.limit.exceeded'


class Computation(object):

    status                  = 'comp.status'
    environments            = 'comp.environments'

    evt_comp_started        = 'comp.started'
    evt_comp_finished       = 'comp.finished'


class Payments(object):

    ident                   = 'pay.ident'

    payments                = 'pay.payments'
    payment                 = 'pay.payment'

    incomes                 = 'pay.incomes'
    income                  = 'pay.income'

    evt_payment             = 'evt.pay.payment'
    evt_income              = 'evt.pay.income'


class UI(object):
    # 'ui'
    pass


class Applications(object):
    # 'app'
    pass


NAMESPACES = [
    Environment,
    Crypto,
    Network,
    Reputation,
    Resources,
    Computation,
    Applications,
    UI,
]

