"===============================================================================
"File: plugin/lxiym.vim
"Maintainer: iamcco <ooiss@qq.com>
"Github: http://github.com/iamcco <年糕小豆汤>
"Licence: Vim Licence
"Version: 1.0.0
"===============================================================================

scriptencoding utf-8

if exists('g:load_lxiym')
    finish
endif
let g:load_lxiym= 1

let s:save_cpo = &cpoptions
set cpoptions&vim

if exists('g:lxiym_lang')
  let g:lxiym_lang = 'zh-cn'
endif


let &cpoptions = s:save_cpo
unlet s:save_cpo
