class Plugin():
    """
    A base class that should be inherited by all other plugins.
    It handles defaults, replacing options and managing lower level
    settings that a plugin developer need not bother with.
    """
    def __init__(self, config, defaults):
        self._outputOptions = {
            'color': None,
            'min_width': None,
            'align': None,
            'name': None,
            'urgent': None,
            'seperator': None,
            'seperator_block_width': None}
        # Replace default values with user defined ones.
        for k, v in config.items():
            self.options[k] = v
            if k in self._outputOptions.keys():
                self._outputOptions[k] = v

    def output(self, fullText, shortText):
        """
        Output all of the options and data for a segment.
        """
        self._outputOptions.update({'full_text': fullText, 'short_text': shortText})
        self._outputOptions = {k: v for k, v in self._outputOptions.items() if v is not None}
        return self._outputOptions