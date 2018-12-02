# ============================================================================
# FILE: lxiym.py
# AUTHOR: 年糕小豆汤 <ooiss@qq.com>
# License: MIT license
# ============================================================================

import os
from .base import Base
from ..kind.base import Base as BaseKind

class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'lxiym'
        self.kind = Kind(vim)

    def on_init(self, context):
        pass

    def gather_candidates(self, context):
        templates_path = self.vim.call('lxiym#get_templates_path')

        if not os.path.isdir(templates_path):
            raise Exception('templates dir is not exists, please check plugin is install complete')

        templates_list = os.listdir(templates_path)
        templates = []

        for template in templates_list:
            names = template.split('.')
            tpath = os.path.join(templates_path, template)
            if not os.path.isdir(tpath):
                templates.append({
                  'word': names[0],
                  'action__path': tpath,
                  'source__path': templates_path,
                })
        return templates

class Kind(BaseKind):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'lxim'
        self.default_action = 'open'
        self.persist_actions = []
        self.redraw_actions = []

    def action_open(self, context):
        target = context['targets'][0]
        lang = self.vim.eval('g:lxiym_lang')
        name = target['word']
        actionPath = target['action__path']
        sourcePath = target['source__path']

        if lang:
            filePath = os.path.join(
                sourcePath,
                '%s/%s-%s.html.markdown' % (lang, name, lang.split('-')[1])
            )
            if os.path.isfile(filePath):
                self.vim.command("edit %s" % filePath)
                return self.vim.command("setlocal readonly")

        self.vim.command("edit %s" % actionPath)
        return self.vim.command("setlocal readonly")
