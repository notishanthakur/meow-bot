from bot import CMD_INDEX


class _BotCommands:
    def __init__(self):
        self.StartCommand = f'start{CMD_INDEX}'
        self.MirrorCommand = f'meow{CMD_INDEX}'
        self.UnzipMirrorCommand = f'unzipmeow{CMD_INDEX}'
        self.ZipMirrorCommand = f'zipmeow{CMD_INDEX}'
        self.CancelMirror = f'cancelmeow{CMD_INDEX}'
        self.CancelAllCommand = f'cancelallmeow{CMD_INDEX}'
        self.ListCommand = f'list{CMD_INDEX}'
        self.SearchCommand = f'searchmeow{CMD_INDEX}'
        self.StatusCommand = f'status{CMD_INDEX}'
        self.AuthorizedUsersCommand = f'users{CMD_INDEX}'
        self.AuthorizeCommand = f'authorize{CMD_INDEX}'
        self.UnAuthorizeCommand = f'unauthorize{CMD_INDEX}'
        self.AddSudoCommand = f'addsudo{CMD_INDEX}'
        self.RmSudoCommand = f'rmsudo{CMD_INDEX}'
        self.PingCommand = f'ping{CMD_INDEX}'
        self.RestartCommand = f'restartcat{CMD_INDEX}'
        self.StatsCommand = f'stats{CMD_INDEX}'
        self.HelpCommand = f'helpcat{CMD_INDEX}'
        self.LogCommand = f'log{CMD_INDEX}'
        self.CloneCommand = f'purr{CMD_INDEX}'
        self.CountCommand = f'countmeow{CMD_INDEX}'
        self.WatchCommand = f'meowyt{CMD_INDEX}'
        self.ZipWatchCommand = f'zipmeowyt{CMD_INDEX}'
        self.QbMirrorCommand = f'qbmeow{CMD_INDEX}'
        self.QbUnzipMirrorCommand = f'qbunzipmeow{CMD_INDEX}'
        self.QbZipMirrorCommand = f'qbzipmeow{CMD_INDEX}'
        self.DeleteCommand = f'meowdel{CMD_INDEX}'
        self.ShellCommand = f'shell{CMD_INDEX}'
        self.ExecHelpCommand = f'exechelp{CMD_INDEX}'
        self.LeechSetCommand = f'leechset{CMD_INDEX}'
        self.SetThumbCommand = f'setthumb{CMD_INDEX}'
        self.LeechCommand = f'leechmeow{CMD_INDEX}'
        self.UnzipLeechCommand = f'unzipleechmeow{CMD_INDEX}'
        self.ZipLeechCommand = f'zipleechmeow{CMD_INDEX}'
        self.QbLeechCommand = f'qbleechmeow{CMD_INDEX}'
        self.QbUnzipLeechCommand = f'qbunzipleechmeow{CMD_INDEX}'
        self.QbZipLeechCommand = f'qbzipleechmeow{CMD_INDEX}'
        self.LeechWatchCommand = f'leechmeowyt{CMD_INDEX}'
        self.LeechZipWatchCommand = f'leechzipmeowyt{CMD_INDEX}'
        self.RssListCommand = f'rsslist{CMD_INDEX}'
        self.RssGetCommand = f'rssget{CMD_INDEX}'
        self.RssSubCommand = f'rsssub{CMD_INDEX}'
        self.RssUnSubCommand = f'rssunsub{CMD_INDEX}'
        self.RssSettingsCommand = f'rssset{CMD_INDEX}'
        self.EvalCommand = f'eval{CMD_INDEX}'
        self.ExecCommand = f'exec{CMD_INDEX}'
        self.ClearLocalsCommand = f'clearlocals{CMD_INDEX}'

BotCommands = _BotCommands()
