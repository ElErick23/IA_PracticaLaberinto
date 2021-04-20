class Handler:

    CALLBACKS = []

    def set_callback(self, type, callback):
        self.CALLBACKS.append({'type': type, 'call': callback})

    def set_callback_list(self, cback_list):
        for cb in cback_list:
            self.set_callback(cb[0], cb[1])


    def exec_callbacks(self, event):
        for c in self.CALLBACKS:
            if c['type'] == event.type:
                c['call'](event)
