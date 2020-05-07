class Progress:
    def __init__(self):
        self.__obs_list = []

    def add_observer(self, obs):
        self.__obs_list.append(obs)

    def notifi(self, *args, **kwargs):
        for obs in self.__obs_list:
            obs.update(*args, **kwargs)

    def list_observer(self):
        return self.__obs_list
