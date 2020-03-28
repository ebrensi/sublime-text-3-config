

import sublime
import sublime_plugin
import os

class ChangeTabColorScheme(sublime_plugin.WindowCommand):

    def run(self):
        window = sublime.active_window()
        view = window.active_view()
        settings = view.settings()

        current_scheme = settings.get('color_scheme', '')
        themes = self.installed_themes()
        names = sorted(themes)

        def make_selection(index):
            name = names[index]
            fname = themes[name]
            settings.set("color_scheme", fname)

        def on_done(index):
	        if index == -1:
	            settings.set("color_scheme", current_scheme)
	            return
	        make_selection(index)

        window.show_quick_panel(
        	names,
        	on_done,
            on_highlight=make_selection
        )

    def installed_themes(self):
        scheme_paths = sublime.find_resources('*.tmTheme')
        scheme_paths.extend(
            sublime.find_resources('*.sublime-color-scheme')
        )

        themes = {os.path.basename(path).split(".")[0]: path for path in scheme_paths}
        return themes

