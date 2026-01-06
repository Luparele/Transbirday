# File Tree: Transbirday

**Generated:** 11/2/2025, 5:49:25 PM
**Root Path:** `c:\Users\lupar\Documents\Transbirday`

```
├── APP
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_seguro.py
│   │   ├── 0003_sinistro.py
│   │   ├── 0004_veiculoassegurado.py
│   │   ├── 0005_alter_historicotarefa_options_alter_tarefa_options_and_more.py
│   │   ├── 0006_certificadoqsms.py
│   │   ├── 0007_agendaqsms.py
│   │   ├── 0008_qsmstarefa_qsmshistoricotarefa.py
│   │   └── __init__.py
│   ├── static
│   │   └── image
│   │       └── logo_transbirday.jpeg
│   ├── templates
│   │   └── APP
│   │       ├── partials
│   │       │   ├── agenda_qsms_edit_form.html
│   │       │   ├── certificado_qsms_edit_form.html
│   │       │   ├── pgr_edit_form.html
│   │       │   ├── seguro_edit_form.html
│   │       │   ├── sinistro_edit_form.html
│   │       │   └── veiculo_assegurado_edit_form.html
│   │       ├── agenda_qsms_list.html
│   │       ├── base.html
│   │       ├── certificado_qsms_list.html
│   │       ├── checklist_view.html
│   │       ├── home.html
│   │       ├── login.html
│   │       ├── password_change.html
│   │       ├── pgr_list.html
│   │       ├── register.html
│   │       ├── rotograma_list.html
│   │       ├── seguro_list.html
│   │       ├── sinistro_list.html
│   │       ├── tarefa_kanban.html
│   │       ├── tarefa_kanban_qsms.html
│   │       ├── tarefa_kanban_security.html
│   │       ├── veiculo_assegurado_list.html
│   │       └── veiculo_list.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── Transbirday_Project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── media
│   ├── pgr_pdfs
│   │   ├── PGR_teste.pdf
│   │   ├── PGR_teste_TZgaXlw.pdf
│   │   ├── PGR_teste_g3uBIQL.pdf
│   │   └── olhos.pdf
│   ├── qsms
│   │   └── certificados_pdf
│   │       └── olhos.pdf
│   ├── rotogramas_pdfs
│   │   ├── PGR_teste.pdf
│   │   └── PGR_teste_RSygxCN.pdf
│   └── seguros
│       ├── apolices
│       │   ├── Apólice_teste.pdf
│       │   └── Apólice_teste_l0RHwmh.pdf
│       └── certificados
│           ├── DDR_teste.pdf
│           └── PGR_teste.pdf
├── pgr_pdfs
│   ├── PGR_teste.pdf
│   ├── PGR_teste_ByjWWpt.pdf
│   ├── PGR_teste_HXpl23b.pdf
│   └── PGR_teste_d4BHvHn.pdf
├── static
├── staticfiles
│   ├── admin
│   │   ├── css
│   │   │   ├── vendor
│   │   │   │   └── select2
│   │   │   │       ├── LICENSE-SELECT2.md
│   │   │   │       └── select2.css
│   │   │   ├── autocomplete.css
│   │   │   ├── base.css
│   │   │   ├── changelists.css
│   │   │   ├── dark_mode.css
│   │   │   ├── dashboard.css
│   │   │   ├── forms.css
│   │   │   ├── login.css
│   │   │   ├── nav_sidebar.css
│   │   │   ├── responsive.css
│   │   │   ├── responsive_rtl.css
│   │   │   ├── rtl.css
│   │   │   ├── unusable_password_field.css
│   │   │   └── widgets.css
│   │   ├── img
│   │   │   ├── gis
│   │   │   │   ├── move_vertex_off.svg
│   │   │   │   └── move_vertex_on.svg
│   │   │   ├── LICENSE
│   │   │   ├── README.txt
│   │   │   ├── calendar-icons.svg
│   │   │   ├── icon-addlink.svg
│   │   │   ├── icon-alert.svg
│   │   │   ├── icon-calendar.svg
│   │   │   ├── icon-changelink.svg
│   │   │   ├── icon-clock.svg
│   │   │   ├── icon-deletelink.svg
│   │   │   ├── icon-hidelink.svg
│   │   │   ├── icon-no.svg
│   │   │   ├── icon-unknown-alt.svg
│   │   │   ├── icon-unknown.svg
│   │   │   ├── icon-viewlink.svg
│   │   │   ├── icon-yes.svg
│   │   │   ├── inline-delete.svg
│   │   │   ├── search.svg
│   │   │   ├── selector-icons.svg
│   │   │   ├── sorting-icons.svg
│   │   │   ├── tooltag-add.svg
│   │   │   └── tooltag-arrowright.svg
│   │   └── js
│   │       ├── admin
│   │       │   ├── DateTimeShortcuts.js
│   │       │   └── RelatedObjectLookups.js
│   │       ├── vendor
│   │       │   ├── jquery
│   │       │   │   ├── LICENSE.txt
│   │       │   │   └── jquery.js
│   │       │   ├── select2
│   │       │   │   ├── i18n
│   │       │   │   │   ├── af.js
│   │       │   │   │   ├── ar.js
│   │       │   │   │   ├── az.js
│   │       │   │   │   ├── bg.js
│   │       │   │   │   ├── bn.js
│   │       │   │   │   ├── bs.js
│   │       │   │   │   ├── ca.js
│   │       │   │   │   ├── cs.js
│   │       │   │   │   ├── da.js
│   │       │   │   │   ├── de.js
│   │       │   │   │   ├── dsb.js
│   │       │   │   │   ├── el.js
│   │       │   │   │   ├── en.js
│   │       │   │   │   ├── es.js
│   │       │   │   │   ├── et.js
│   │       │   │   │   ├── eu.js
│   │       │   │   │   ├── fa.js
│   │       │   │   │   ├── fi.js
│   │       │   │   │   ├── fr.js
│   │       │   │   │   ├── gl.js
│   │       │   │   │   ├── he.js
│   │       │   │   │   ├── hi.js
│   │       │   │   │   ├── hr.js
│   │       │   │   │   ├── hsb.js
│   │       │   │   │   ├── hu.js
│   │       │   │   │   ├── hy.js
│   │       │   │   │   ├── id.js
│   │       │   │   │   ├── is.js
│   │       │   │   │   ├── it.js
│   │       │   │   │   ├── ja.js
│   │       │   │   │   ├── ka.js
│   │       │   │   │   ├── km.js
│   │       │   │   │   ├── ko.js
│   │       │   │   │   ├── lt.js
│   │       │   │   │   ├── lv.js
│   │       │   │   │   ├── mk.js
│   │       │   │   │   ├── ms.js
│   │       │   │   │   ├── nb.js
│   │       │   │   │   ├── ne.js
│   │       │   │   │   ├── nl.js
│   │       │   │   │   ├── pl.js
│   │       │   │   │   ├── ps.js
│   │       │   │   │   ├── pt-BR.js
│   │       │   │   │   ├── pt.js
│   │       │   │   │   ├── ro.js
│   │       │   │   │   ├── ru.js
│   │       │   │   │   ├── sk.js
│   │       │   │   │   ├── sl.js
│   │       │   │   │   ├── sq.js
│   │       │   │   │   ├── sr-Cyrl.js
│   │       │   │   │   ├── sr.js
│   │       │   │   │   ├── sv.js
│   │       │   │   │   ├── th.js
│   │       │   │   │   ├── tk.js
│   │       │   │   │   ├── tr.js
│   │       │   │   │   ├── uk.js
│   │       │   │   │   ├── vi.js
│   │       │   │   │   ├── zh-CN.js
│   │       │   │   │   └── zh-TW.js
│   │       │   │   ├── LICENSE.md
│   │       │   │   └── select2.full.js
│   │       │   └── xregexp
│   │       │       ├── LICENSE.txt
│   │       │       └── xregexp.js
│   │       ├── SelectBox.js
│   │       ├── SelectFilter2.js
│   │       ├── actions.js
│   │       ├── autocomplete.js
│   │       ├── calendar.js
│   │       ├── cancel.js
│   │       ├── change_form.js
│   │       ├── core.js
│   │       ├── filters.js
│   │       ├── inlines.js
│   │       ├── jquery.init.js
│   │       ├── nav_sidebar.js
│   │       ├── popup_response.js
│   │       ├── prepopulate.js
│   │       ├── prepopulate_init.js
│   │       ├── theme.js
│   │       ├── unusable_password_field.js
│   │       └── urlify.js
│   └── ckeditor
│       ├── ckeditor
│       │   ├── adapters
│       │   │   └── jquery.js
│       │   ├── lang
│       │   │   ├── af.js
│       │   │   ├── ar.js
│       │   │   ├── az.js
│       │   │   ├── bg.js
│       │   │   ├── bn.js
│       │   │   ├── bs.js
│       │   │   ├── ca.js
│       │   │   ├── cs.js
│       │   │   ├── cy.js
│       │   │   ├── da.js
│       │   │   ├── de-ch.js
│       │   │   ├── de.js
│       │   │   ├── el.js
│       │   │   ├── en-au.js
│       │   │   ├── en-ca.js
│       │   │   ├── en-gb.js
│       │   │   ├── en.js
│       │   │   ├── eo.js
│       │   │   ├── es-mx.js
│       │   │   ├── es.js
│       │   │   ├── et.js
│       │   │   ├── eu.js
│       │   │   ├── fa.js
│       │   │   ├── fi.js
│       │   │   ├── fo.js
│       │   │   ├── fr-ca.js
│       │   │   ├── fr.js
│       │   │   ├── gl.js
│       │   │   ├── gu.js
│       │   │   ├── he.js
│       │   │   ├── hi.js
│       │   │   ├── hr.js
│       │   │   ├── hu.js
│       │   │   ├── id.js
│       │   │   ├── is.js
│       │   │   ├── it.js
│       │   │   ├── ja.js
│       │   │   ├── ka.js
│       │   │   ├── km.js
│       │   │   ├── ko.js
│       │   │   ├── ku.js
│       │   │   ├── lt.js
│       │   │   ├── lv.js
│       │   │   ├── mk.js
│       │   │   ├── mn.js
│       │   │   ├── ms.js
│       │   │   ├── nb.js
│       │   │   ├── nl.js
│       │   │   ├── no.js
│       │   │   ├── oc.js
│       │   │   ├── pl.js
│       │   │   ├── pt-br.js
│       │   │   ├── pt.js
│       │   │   ├── ro.js
│       │   │   ├── ru.js
│       │   │   ├── si.js
│       │   │   ├── sk.js
│       │   │   ├── sl.js
│       │   │   ├── sq.js
│       │   │   ├── sr-latn.js
│       │   │   ├── sr.js
│       │   │   ├── sv.js
│       │   │   ├── th.js
│       │   │   ├── tr.js
│       │   │   ├── tt.js
│       │   │   ├── ug.js
│       │   │   ├── uk.js
│       │   │   ├── vi.js
│       │   │   ├── zh-cn.js
│       │   │   └── zh.js
│       │   ├── plugins
│       │   │   ├── a11yhelp
│       │   │   │   └── dialogs
│       │   │   │       ├── lang
│       │   │   │       │   ├── _translationstatus.txt
│       │   │   │       │   ├── af.js
│       │   │   │       │   ├── ar.js
│       │   │   │       │   ├── az.js
│       │   │   │       │   ├── bg.js
│       │   │   │       │   ├── ca.js
│       │   │   │       │   ├── cs.js
│       │   │   │       │   ├── cy.js
│       │   │   │       │   ├── da.js
│       │   │   │       │   ├── de-ch.js
│       │   │   │       │   ├── de.js
│       │   │   │       │   ├── el.js
│       │   │   │       │   ├── en-au.js
│       │   │   │       │   ├── en-gb.js
│       │   │   │       │   ├── en.js
│       │   │   │       │   ├── eo.js
│       │   │   │       │   ├── es-mx.js
│       │   │   │       │   ├── es.js
│       │   │   │       │   ├── et.js
│       │   │   │       │   ├── eu.js
│       │   │   │       │   ├── fa.js
│       │   │   │       │   ├── fi.js
│       │   │   │       │   ├── fo.js
│       │   │   │       │   ├── fr-ca.js
│       │   │   │       │   ├── fr.js
│       │   │   │       │   ├── gl.js
│       │   │   │       │   ├── gu.js
│       │   │   │       │   ├── he.js
│       │   │   │       │   ├── hi.js
│       │   │   │       │   ├── hr.js
│       │   │   │       │   ├── hu.js
│       │   │   │       │   ├── id.js
│       │   │   │       │   ├── it.js
│       │   │   │       │   ├── ja.js
│       │   │   │       │   ├── km.js
│       │   │   │       │   ├── ko.js
│       │   │   │       │   ├── ku.js
│       │   │   │       │   ├── lt.js
│       │   │   │       │   ├── lv.js
│       │   │   │       │   ├── mk.js
│       │   │   │       │   ├── mn.js
│       │   │   │       │   ├── nb.js
│       │   │   │       │   ├── nl.js
│       │   │   │       │   ├── no.js
│       │   │   │       │   ├── oc.js
│       │   │   │       │   ├── pl.js
│       │   │   │       │   ├── pt-br.js
│       │   │   │       │   ├── pt.js
│       │   │   │       │   ├── ro.js
│       │   │   │       │   ├── ru.js
│       │   │   │       │   ├── si.js
│       │   │   │       │   ├── sk.js
│       │   │   │       │   ├── sl.js
│       │   │   │       │   ├── sq.js
│       │   │   │       │   ├── sr-latn.js
│       │   │   │       │   ├── sr.js
│       │   │   │       │   ├── sv.js
│       │   │   │       │   ├── th.js
│       │   │   │       │   ├── tr.js
│       │   │   │       │   ├── tt.js
│       │   │   │       │   ├── ug.js
│       │   │   │       │   ├── uk.js
│       │   │   │       │   ├── vi.js
│       │   │   │       │   ├── zh-cn.js
│       │   │   │       │   └── zh.js
│       │   │   │       └── a11yhelp.js
│       │   │   ├── about
│       │   │   │   └── dialogs
│       │   │   │       ├── hidpi
│       │   │   │       │   └── logo_ckeditor.png
│       │   │   │       ├── about.js
│       │   │   │       └── logo_ckeditor.png
│       │   │   ├── adobeair
│       │   │   │   └── plugin.js
│       │   │   ├── ajax
│       │   │   │   └── plugin.js
│       │   │   ├── autoembed
│       │   │   │   ├── lang
│       │   │   │   │   ├── cs.js
│       │   │   │   │   ├── de.js
│       │   │   │   │   ├── en.js
│       │   │   │   │   ├── it.js
│       │   │   │   │   ├── ku.js
│       │   │   │   │   ├── nb.js
│       │   │   │   │   ├── pl.js
│       │   │   │   │   ├── pt-br.js
│       │   │   │   │   ├── tr.js
│       │   │   │   │   └── zh.js
│       │   │   │   └── plugin.js
│       │   │   ├── autogrow
│       │   │   │   └── plugin.js
│       │   │   ├── autolink
│       │   │   │   └── plugin.js
│       │   │   ├── bbcode
│       │   │   │   └── plugin.js
│       │   │   ├── clipboard
│       │   │   │   └── dialogs
│       │   │   │       └── paste.js
│       │   │   ├── codesnippet
│       │   │   │   ├── dialogs
│       │   │   │   │   └── codesnippet.js
│       │   │   │   ├── icons
│       │   │   │   │   ├── hidpi
│       │   │   │   │   │   └── codesnippet.png
│       │   │   │   │   └── codesnippet.png
│       │   │   │   ├── lang
│       │   │   │   │   ├── ar.js
│       │   │   │   │   ├── bg.js
│       │   │   │   │   ├── ca.js
│       │   │   │   │   ├── cs.js
│       │   │   │   │   ├── da.js
│       │   │   │   │   ├── de.js
│       │   │   │   │   ├── el.js
│       │   │   │   │   ├── en-gb.js
│       │   │   │   │   ├── en.js
│       │   │   │   │   ├── eo.js
│       │   │   │   │   ├── es.js
│       │   │   │   │   ├── et.js
│       │   │   │   │   ├── fa.js
│       │   │   │   │   ├── fi.js
│       │   │   │   │   ├── fr-ca.js
│       │   │   │   │   ├── fr.js
│       │   │   │   │   ├── gl.js
│       │   │   │   │   ├── he.js
│       │   │   │   │   ├── hr.js
│       │   │   │   │   ├── hu.js
│       │   │   │   │   ├── it.js
│       │   │   │   │   ├── ja.js
│       │   │   │   │   ├── km.js
│       │   │   │   │   ├── ko.js
│       │   │   │   │   ├── ku.js
│       │   │   │   │   ├── lt.js
│       │   │   │   │   ├── lv.js
│       │   │   │   │   ├── nb.js
│       │   │   │   │   ├── nl.js
│       │   │   │   │   ├── no.js
│       │   │   │   │   ├── pl.js
│       │   │   │   │   ├── pt-br.js
│       │   │   │   │   ├── pt.js
│       │   │   │   │   ├── ro.js
│       │   │   │   │   ├── ru.js
│       │   │   │   │   ├── sk.js
│       │   │   │   │   ├── sl.js
│       │   │   │   │   ├── sq.js
│       │   │   │   │   ├── sv.js
│       │   │   │   │   ├── th.js
│       │   │   │   │   ├── tr.js
│       │   │   │   │   ├── tt.js
│       │   │   │   │   ├── ug.js
│       │   │   │   │   ├── uk.js
│       │   │   │   │   ├── vi.js
│       │   │   │   │   ├── zh-cn.js
│       │   │   │   │   └── zh.js
│       │   │   │   ├── lib
│       │   │   │   │   └── highlight
│       │   │   │   │       ├── styles
│       │   │   │   │       │   ├── arta.css
│       │   │   │   │       │   ├── ascetic.css
│       │   │   │   │       │   ├── atelier-dune.dark.css
│       │   │   │   │       │   ├── atelier-dune.light.css
│       │   │   │   │       │   ├── atelier-forest.dark.css
│       │   │   │   │       │   ├── atelier-forest.light.css
│       │   │   │   │       │   ├── atelier-heath.dark.css
│       │   │   │   │       │   ├── atelier-heath.light.css
│       │   │   │   │       │   ├── atelier-lakeside.dark.css
│       │   │   │   │       │   ├── atelier-lakeside.light.css
│       │   │   │   │       │   ├── atelier-seaside.dark.css
│       │   │   │   │       │   ├── atelier-seaside.light.css
│       │   │   │   │       │   ├── brown_paper.css
│       │   │   │   │       │   ├── brown_papersq.png
│       │   │   │   │       │   ├── dark.css
│       │   │   │   │       │   ├── default.css
│       │   │   │   │       │   ├── docco.css
│       │   │   │   │       │   ├── far.css
│       │   │   │   │       │   ├── foundation.css
│       │   │   │   │       │   ├── github.css
│       │   │   │   │       │   ├── googlecode.css
│       │   │   │   │       │   ├── idea.css
│       │   │   │   │       │   ├── ir_black.css
│       │   │   │   │       │   ├── magula.css
│       │   │   │   │       │   ├── mono-blue.css
│       │   │   │   │       │   ├── monokai.css
│       │   │   │   │       │   ├── monokai_sublime.css
│       │   │   │   │       │   ├── obsidian.css
│       │   │   │   │       │   ├── paraiso.dark.css
│       │   │   │   │       │   ├── paraiso.light.css
│       │   │   │   │       │   ├── pojoaque.css
│       │   │   │   │       │   ├── pojoaque.jpg
│       │   │   │   │       │   ├── railscasts.css
│       │   │   │   │       │   ├── rainbow.css
│       │   │   │   │       │   ├── school_book.css
│       │   │   │   │       │   ├── school_book.png
│       │   │   │   │       │   ├── solarized_dark.css
│       │   │   │   │       │   ├── solarized_light.css
│       │   │   │   │       │   ├── sunburst.css
│       │   │   │   │       │   ├── tomorrow-night-blue.css
│       │   │   │   │       │   ├── tomorrow-night-bright.css
│       │   │   │   │       │   ├── tomorrow-night-eighties.css
│       │   │   │   │       │   ├── tomorrow-night.css
│       │   │   │   │       │   ├── tomorrow.css
│       │   │   │   │       │   ├── vs.css
│       │   │   │   │       │   ├── xcode.css
│       │   │   │   │       │   └── zenburn.css
│       │   │   │   │       ├── CHANGES.md
│       │   │   │   │       ├── LICENSE
│       │   │   │   │       ├── README.ru.md
│       │   │   │   │       └── highlight.pack.js
│       │   │   │   └── plugin.js
│       │   │   ├── codesnippetgeshi
│       │   │   │   └── plugin.js
│       │   │   ├── colordialog
│       │   │   │   └── dialogs
│       │   │   │       ├── colordialog.css
│       │   │   │       └── colordialog.js
│       │   │   ├── copyformatting
│       │   │   │   ├── cursors
│       │   │   │   │   ├── cursor-disabled.svg
│       │   │   │   │   └── cursor.svg
│       │   │   │   └── styles
│       │   │   │       └── copyformatting.css
│       │   │   ├── devtools
│       │   │   │   ├── lang
│       │   │   │   │   ├── _translationstatus.txt
│       │   │   │   │   ├── ar.js
│       │   │   │   │   ├── bg.js
│       │   │   │   │   ├── ca.js
│       │   │   │   │   ├── cs.js
│       │   │   │   │   ├── cy.js
│       │   │   │   │   ├── da.js
│       │   │   │   │   ├── de.js
│       │   │   │   │   ├── el.js
│       │   │   │   │   ├── en-gb.js
│       │   │   │   │   ├── en.js
│       │   │   │   │   ├── eo.js
│       │   │   │   │   ├── es.js
│       │   │   │   │   ├── et.js
│       │   │   │   │   ├── eu.js
│       │   │   │   │   ├── fa.js
│       │   │   │   │   ├── fi.js
│       │   │   │   │   ├── fr-ca.js
│       │   │   │   │   ├── fr.js
│       │   │   │   │   ├── gl.js
│       │   │   │   │   ├── gu.js
│       │   │   │   │   ├── he.js
│       │   │   │   │   ├── hr.js
│       │   │   │   │   ├── hu.js
│       │   │   │   │   ├── id.js
│       │   │   │   │   ├── it.js
│       │   │   │   │   ├── ja.js
│       │   │   │   │   ├── km.js
│       │   │   │   │   ├── ko.js
│       │   │   │   │   ├── ku.js
│       │   │   │   │   ├── lt.js
│       │   │   │   │   ├── lv.js
│       │   │   │   │   ├── nb.js
│       │   │   │   │   ├── nl.js
│       │   │   │   │   ├── no.js
│       │   │   │   │   ├── pl.js
│       │   │   │   │   ├── pt-br.js
│       │   │   │   │   ├── pt.js
│       │   │   │   │   ├── ro.js
│       │   │   │   │   ├── ru.js
│       │   │   │   │   ├── si.js
│       │   │   │   │   ├── sk.js
│       │   │   │   │   ├── sl.js
│       │   │   │   │   ├── sq.js
│       │   │   │   │   ├── sv.js
│       │   │   │   │   ├── tr.js
│       │   │   │   │   ├── tt.js
│       │   │   │   │   ├── ug.js
│       │   │   │   │   ├── uk.js
│       │   │   │   │   ├── vi.js
│       │   │   │   │   ├── zh-cn.js
│       │   │   │   │   └── zh.js
│       │   │   │   └── plugin.js
│       │   │   ├── dialog
│       │   │   │   ├── styles
│       │   │   │   │   └── dialog.css
│       │   │   │   └── dialogDefinition.js
│       │   │   ├── div
│       │   │   │   └── dialogs
│       │   │   │       └── div.js
│       │   │   ├── divarea
│       │   │   │   └── plugin.js
│       │   │   ├── docprops
│       │   │   │   ├── dialogs
│       │   │   │   │   └── docprops.js
│       │   │   │   ├── icons
│       │   │   │   │   ├── hidpi
│       │   │   │   │   │   ├── docprops-rtl.png
│       │   │   │   │   │   └── docprops.png
│       │   │   │   │   ├── docprops-rtl.png
│       │   │   │   │   └── docprops.png
│       │   │   │   ├── lang
│       │   │   │   │   ├── af.js
│       │   │   │   │   ├── ar.js
│       │   │   │   │   ├── bg.js
│       │   │   │   │   ├── bn.js
│       │   │   │   │   ├── bs.js
│       │   │   │   │   ├── ca.js
│       │   │   │   │   ├── cs.js
│       │   │   │   │   ├── cy.js
│       │   │   │   │   ├── da.js
│       │   │   │   │   ├── de.js
│       │   │   │   │   ├── el.js
│       │   │   │   │   ├── en-au.js
│       │   │   │   │   ├── en-ca.js
│       │   │   │   │   ├── en-gb.js
│       │   │   │   │   ├── en.js
│       │   │   │   │   ├── eo.js
│       │   │   │   │   ├── es.js
│       │   │   │   │   ├── et.js
│       │   │   │   │   ├── eu.js
│       │   │   │   │   ├── fa.js
│       │   │   │   │   ├── fi.js
│       │   │   │   │   ├── fo.js
│       │   │   │   │   ├── fr-ca.js
│       │   │   │   │   ├── fr.js
│       │   │   │   │   ├── gl.js
│       │   │   │   │   ├── gu.js
│       │   │   │   │   ├── he.js
│       │   │   │   │   ├── hi.js
│       │   │   │   │   ├── hr.js
│       │   │   │   │   ├── hu.js
│       │   │   │   │   ├── id.js
│       │   │   │   │   ├── is.js
│       │   │   │   │   ├── it.js
│       │   │   │   │   ├── ja.js
│       │   │   │   │   ├── ka.js
│       │   │   │   │   ├── km.js
│       │   │   │   │   ├── ko.js
│       │   │   │   │   ├── ku.js
│       │   │   │   │   ├── lt.js
│       │   │   │   │   ├── lv.js
│       │   │   │   │   ├── mk.js
│       │   │   │   │   ├── mn.js
│       │   │   │   │   ├── ms.js
│       │   │   │   │   ├── nb.js
│       │   │   │   │   ├── nl.js
│       │   │   │   │   ├── no.js
│       │   │   │   │   ├── pl.js
│       │   │   │   │   ├── pt-br.js
│       │   │   │   │   ├── pt.js
│       │   │   │   │   ├── ro.js
│       │   │   │   │   ├── ru.js
│       │   │   │   │   ├── si.js
│       │   │   │   │   ├── sk.js
│       │   │   │   │   ├── sl.js
│       │   │   │   │   ├── sq.js
│       │   │   │   │   ├── sr-latn.js
│       │   │   │   │   ├── sr.js
│       │   │   │   │   ├── sv.js
│       │   │   │   │   ├── th.js
│       │   │   │   │   ├── tr.js
│       │   │   │   │   ├── tt.js
│       │   │   │   │   ├── ug.js
│       │   │   │   │   ├── uk.js
│       │   │   │   │   ├── vi.js
│       │   │   │   │   ├── zh-cn.js
│       │   │   │   │   └── zh.js
│       │   │   │   └── plugin.js
│       │   │   ├── embed
│       │   │   │   ├── icons
│       │   │   │   │   ├── hidpi
│       │   │   │   │   │   └── embed.png
│       │   │   │   │   └── embed.png
│       │   │   │   └── plugin.js
│       │   │   ├── embedbase
│       │   │   │   ├── dialogs
│       │   │   │   │   └── embedbase.js
│       │   │   │   ├── lang
│       │   │   │   │   ├── cs.js
│       │   │   │   │   ├── da.js
│       │   │   │   │   ├── de.js
│       │   │   │   │   ├── en.js
│       │   │   │   │   ├── eo.js
│       │   │   │   │   ├── fr.js
│       │   │   │   │   ├── gl.js
│       │   │   │   │   ├── it.js
│       │   │   │   │   ├── ko.js
│       │   │   │   │   ├── ku.js
│       │   │   │   │   ├── nb.js
│       │   │   │   │   ├── nl.js
│       │   │   │   │   ├── pl.js
│       │   │   │   │   ├── pt-br.js
│       │   │   │   │   ├── ru.js
│       │   │   │   │   ├── sv.js
│       │   │   │   │   ├── tr.js
│       │   │   │   │   ├── zh-cn.js
│       │   │   │   │   └── zh.js
│       │   │   │   └── plugin.js
│       │   │   ├── embedsemantic
│       │   │   │   ├── icons
│       │   │   │   │   ├── hidpi
│       │   │   │   │   │   └── embedsemantic.png
│       │   │   │   │   └── embedsemantic.png
│       │   │   │   └── plugin.js
│       │   │   ├── exportpdf
│       │   │   │   ├── tests
│       │   │   │   │   ├── _helpers
│       │   │   │   │   │   └── tools.js
│       │   │   │   │   ├── manual
│       │   │   │   │   │   ├── integrations
│       │   │   │   │   │   │   ├── easyimage.html
│       │   │   │   │   │   │   └── easyimage.md
│       │   │   │   │   │   ├── configfilename.html
│       │   │   │   │   │   ├── configfilename.md
│       │   │   │   │   │   ├── emptyeditor.html
│       │   │   │   │   │   ├── emptyeditor.md
│       │   │   │   │   │   ├── integration.html
│       │   │   │   │   │   ├── integration.md
│       │   │   │   │   │   ├── notifications.html
│       │   │   │   │   │   ├── notifications.md
│       │   │   │   │   │   ├── notificationsasync.html
│       │   │   │   │   │   ├── notificationsasync.md
│       │   │   │   │   │   ├── paperformat.html
│       │   │   │   │   │   ├── paperformat.md
│       │   │   │   │   │   ├── readonly.html
│       │   │   │   │   │   ├── readonly.md
│       │   │   │   │   │   ├── stylesheets.html
│       │   │   │   │   │   ├── stylesheets.md
│       │   │   │   │   │   ├── tokenfetching.html
│       │   │   │   │   │   ├── tokenfetching.md
│       │   │   │   │   │   ├── tokentwoeditorscorrect.html
│       │   │   │   │   │   ├── tokentwoeditorscorrect.md
│       │   │   │   │   │   ├── tokentwoeditorswrong.html
│       │   │   │   │   │   ├── tokentwoeditorswrong.md
│       │   │   │   │   │   ├── tokenwithouturl.html
│       │   │   │   │   │   ├── tokenwithouturl.md
│       │   │   │   │   │   ├── wrongendpoint.html
│       │   │   │   │   │   └── wrongendpoint.md
│       │   │   │   │   ├── authentication.js
│       │   │   │   │   ├── exportpdf.js
│       │   │   │   │   ├── notification.js
│       │   │   │   │   ├── resourcespaths.js
│       │   │   │   │   ├── statistics.js
│       │   │   │   │   └── stylesheets.js
│       │   │   │   ├── CHANGELOG.md
│       │   │   │   ├── LICENSE.md
│       │   │   │   ├── README.md
│       │   │   │   └── plugindefinition.js
│       │   │   ├── filetools
│       │   │   │   ├── lang
│       │   │   │   │   ├── cs.js
│       │   │   │   │   ├── da.js
│       │   │   │   │   ├── de.js
│       │   │   │   │   ├── en.js
│       │   │   │   │   ├── eo.js
│       │   │   │   │   ├── fr.js
│       │   │   │   │   ├── gl.js
│       │   │   │   │   ├── it.js
│       │   │   │   │   ├── ko.js
│       │   │   │   │   ├── ku.js
│       │   │   │   │   ├── nb.js
│       │   │   │   │   ├── nl.js
│       │   │   │   │   ├── pl.js
│       │   │   │   │   ├── pt-br.js
│       │   │   │   │   ├── ru.js
│       │   │   │   │   ├── sv.js
│       │   │   │   │   ├── tr.js
│       │   │   │   │   ├── zh-cn.js
│       │   │   │   │   └── zh.js
│       │   │   │   └── plugin.js
│       │   │   ├── find
│       │   │   │   └── dialogs
│       │   │   │       └── find.js
│       │   │   ├── flash
│       │   │   │   ├── dialogs
│       │   │   │   │   └── flash.js
│       │   │   │   └── images
│       │   │   │       └── placeholder.png
│       │   │   ├── forms
│       │   │   │   ├── dialogs
│       │   │   │   │   ├── button.js
│       │   │   │   │   ├── checkbox.js
│       │   │   │   │   ├── form.js
│       │   │   │   │   ├── hiddenfield.js
│       │   │   │   │   ├── radio.js
│       │   │   │   │   ├── select.js
│       │   │   │   │   ├── textarea.js
│       │   │   │   │   └── textfield.js
│       │   │   │   └── images
│       │   │   │       └── hiddenfield.gif
│       │   │   ├── iframe
│       │   │   │   ├── dialogs
│       │   │   │   │   └── iframe.js
│       │   │   │   └── images
│       │   │   │       └── placeholder.png
│       │   │   ├── iframedialog
│       │   │   │   └── plugin.js
│       │   │   ├── image
│       │   │   │   ├── dialogs
│       │   │   │   │   └── image.js
│       │   │   │   └── images
│       │   │   │       └── noimage.png
│       │   │   ├── image2
│       │   │   │   ├── dialogs
│       │   │   │   │   └── image2.js
│       │   │   │   ├── icons
│       │   │   │   │   ├── hidpi
│       │   │   │   │   │   └── image.png
│       │   │   │   │   └── image.png
│       │   │   │   ├── lang
│       │   │   │   │   ├── af.js
│       │   │   │   │   ├── ar.js
│       │   │   │   │   ├── bg.js
│       │   │   │   │   ├── bn.js
│       │   │   │   │   ├── bs.js
│       │   │   │   │   ├── ca.js
│       │   │   │   │   ├── cs.js
│       │   │   │   │   ├── cy.js
│       │   │   │   │   ├── da.js
│       │   │   │   │   ├── de.js
│       │   │   │   │   ├── el.js
│       │   │   │   │   ├── en-au.js
│       │   │   │   │   ├── en-ca.js
│       │   │   │   │   ├── en-gb.js
│       │   │   │   │   ├── en.js
│       │   │   │   │   ├── eo.js
│       │   │   │   │   ├── es.js
│       │   │   │   │   ├── et.js
│       │   │   │   │   ├── eu.js
│       │   │   │   │   ├── fa.js
│       │   │   │   │   ├── fi.js
│       │   │   │   │   ├── fo.js
│       │   │   │   │   ├── fr-ca.js
│       │   │   │   │   ├── fr.js
│       │   │   │   │   ├── gl.js
│       │   │   │   │   ├── gu.js
│       │   │   │   │   ├── he.js
│       │   │   │   │   ├── hi.js
│       │   │   │   │   ├── hr.js
│       │   │   │   │   ├── hu.js
│       │   │   │   │   ├── id.js
│       │   │   │   │   ├── is.js
│       │   │   │   │   ├── it.js
│       │   │   │   │   ├── ja.js
│       │   │   │   │   ├── ka.js
│       │   │   │   │   ├── km.js
│       │   │   │   │   ├── ko.js
│       │   │   │   │   ├── ku.js
│       │   │   │   │   ├── lt.js
│       │   │   │   │   ├── lv.js
│       │   │   │   │   ├── mk.js
│       │   │   │   │   ├── mn.js
│       │   │   │   │   ├── ms.js
│       │   │   │   │   ├── nb.js
│       │   │   │   │   ├── nl.js
│       │   │   │   │   ├── no.js
│       │   │   │   │   ├── pl.js
│       │   │   │   │   ├── pt-br.js
│       │   │   │   │   ├── pt.js
│       │   │   │   │   ├── ro.js
│       │   │   │   │   ├── ru.js
│       │   │   │   │   ├── si.js
│       │   │   │   │   ├── sk.js
│       │   │   │   │   ├── sl.js
│       │   │   │   │   ├── sq.js
│       │   │   │   │   ├── sr-latn.js
│       │   │   │   │   ├── sr.js
│       │   │   │   │   ├── sv.js
│       │   │   │   │   ├── th.js
│       │   │   │   │   ├── tr.js
│       │   │   │   │   ├── tt.js
│       │   │   │   │   ├── ug.js
│       │   │   │   │   ├── uk.js
│       │   │   │   │   ├── vi.js
│       │   │   │   │   ├── zh-cn.js
│       │   │   │   │   └── zh.js
│       │   │   │   └── plugin.js
│       │   │   ├── language
│       │   │   │   ├── icons
│       │   │   │   │   ├── hidpi
│       │   │   │   │   │   └── language.png
│       │   │   │   │   └── language.png
│       │   │   │   ├── lang
│       │   │   │   │   ├── ar.js
│       │   │   │   │   ├── bg.js
│       │   │   │   │   ├── ca.js
│       │   │   │   │   ├── cs.js
│       │   │   │   │   ├── cy.js
│       │   │   │   │   ├── da.js
│       │   │   │   │   ├── de.js
│       │   │   │   │   ├── el.js
│       │   │   │   │   ├── en-gb.js
│       │   │   │   │   ├── en.js
│       │   │   │   │   ├── eo.js
│       │   │   │   │   ├── es.js
│       │   │   │   │   ├── fa.js
│       │   │   │   │   ├── fi.js
│       │   │   │   │   ├── fo.js
│       │   │   │   │   ├── fr.js
│       │   │   │   │   ├── gl.js
│       │   │   │   │   ├── he.js
│       │   │   │   │   ├── hr.js
│       │   │   │   │   ├── hu.js
│       │   │   │   │   ├── it.js
│       │   │   │   │   ├── ja.js
│       │   │   │   │   ├── km.js
│       │   │   │   │   ├── ko.js
│       │   │   │   │   ├── ku.js
│       │   │   │   │   ├── nb.js
│       │   │   │   │   ├── nl.js
│       │   │   │   │   ├── no.js
│       │   │   │   │   ├── pl.js
│       │   │   │   │   ├── pt-br.js
│       │   │   │   │   ├── pt.js
│       │   │   │   │   ├── ru.js
│       │   │   │   │   ├── sk.js
│       │   │   │   │   ├── sl.js
│       │   │   │   │   ├── sq.js
│       │   │   │   │   ├── sv.js
│       │   │   │   │   ├── tr.js
│       │   │   │   │   ├── tt.js
│       │   │   │   │   ├── uk.js
│       │   │   │   │   ├── vi.js
│       │   │   │   │   ├── zh-cn.js
│       │   │   │   │   └── zh.js
│       │   │   │   └── plugin.js
│       │   │   ├── lineutils
│       │   │   │   └── plugin.js
│       │   │   ├── link
│       │   │   │   ├── dialogs
│       │   │   │   │   ├── anchor.js
│       │   │   │   │   └── link.js
│       │   │   │   └── images
│       │   │   │       ├── hidpi
│       │   │   │       │   └── anchor.png
│       │   │   │       └── anchor.png
│       │   │   ├── liststyle
│       │   │   │   └── dialogs
│       │   │   │       └── liststyle.js
│       │   │   ├── magicline
│       │   │   │   └── images
│       │   │   │       ├── hidpi
│       │   │   │       │   ├── icon-rtl.png
│       │   │   │       │   └── icon.png
│       │   │   │       ├── icon-rtl.png
│       │   │   │       └── icon.png
│       │   │   ├── mathjax
│       │   │   │   ├── dialogs
│       │   │   │   │   └── mathjax.js
│       │   │   │   ├── icons
│       │   │   │   │   ├── hidpi
│       │   │   │   │   │   └── mathjax.png
│       │   │   │   │   └── mathjax.png
│       │   │   │   ├── images
│       │   │   │   │   └── loader.gif
│       │   │   │   ├── lang
│       │   │   │   │   ├── af.js
│       │   │   │   │   ├── ar.js
│       │   │   │   │   ├── bg.js
│       │   │   │   │   ├── ca.js
│       │   │   │   │   ├── cs.js
│       │   │   │   │   ├── cy.js
│       │   │   │   │   ├── da.js
│       │   │   │   │   ├── de.js
│       │   │   │   │   ├── el.js
│       │   │   │   │   ├── en-gb.js
│       │   │   │   │   ├── en.js
│       │   │   │   │   ├── eo.js
│       │   │   │   │   ├── es.js
│       │   │   │   │   ├── fa.js
│       │   │   │   │   ├── fi.js
│       │   │   │   │   ├── fr.js
│       │   │   │   │   ├── gl.js
│       │   │   │   │   ├── he.js
│       │   │   │   │   ├── hr.js
│       │   │   │   │   ├── hu.js
│       │   │   │   │   ├── it.js
│       │   │   │   │   ├── ja.js
│       │   │   │   │   ├── km.js
│       │   │   │   │   ├── ko.js
│       │   │   │   │   ├── ku.js
│       │   │   │   │   ├── lt.js
│       │   │   │   │   ├── nb.js
│       │   │   │   │   ├── nl.js
│       │   │   │   │   ├── no.js
│       │   │   │   │   ├── pl.js
│       │   │   │   │   ├── pt-br.js
│       │   │   │   │   ├── pt.js
│       │   │   │   │   ├── ro.js
│       │   │   │   │   ├── ru.js
│       │   │   │   │   ├── sk.js
│       │   │   │   │   ├── sl.js
│       │   │   │   │   ├── sq.js
│       │   │   │   │   ├── sv.js
│       │   │   │   │   ├── tr.js
│       │   │   │   │   ├── tt.js
│       │   │   │   │   ├── uk.js
│       │   │   │   │   ├── vi.js
│       │   │   │   │   ├── zh-cn.js
│       │   │   │   │   └── zh.js
│       │   │   │   └── plugin.js
│       │   │   ├── menubutton
│       │   │   │   └── plugin.js
│       │   │   ├── notification
│       │   │   │   ├── lang
│       │   │   │   │   ├── cs.js
│       │   │   │   │   ├── da.js
│       │   │   │   │   ├── de.js
│       │   │   │   │   ├── en.js
│       │   │   │   │   ├── eo.js
│       │   │   │   │   ├── fr.js
│       │   │   │   │   ├── gl.js
│       │   │   │   │   ├── it.js
│       │   │   │   │   ├── ko.js
│       │   │   │   │   ├── ku.js
│       │   │   │   │   ├── nb.js
│       │   │   │   │   ├── nl.js
│       │   │   │   │   ├── pl.js
│       │   │   │   │   ├── pt-br.js
│       │   │   │   │   ├── ru.js
│       │   │   │   │   ├── sv.js
│       │   │   │   │   ├── tr.js
│       │   │   │   │   ├── zh-cn.js
│       │   │   │   │   └── zh.js
│       │   │   │   └── plugin.js
│       │   │   ├── notificationaggregator
│       │   │   │   └── plugin.js
│       │   │   ├── pagebreak
│       │   │   │   └── images
│       │   │   │       └── pagebreak.gif
│       │   │   ├── pastefromgdocs
│       │   │   │   └── filter
│       │   │   │       └── default.js
│       │   │   ├── pastefromlibreoffice
│       │   │   │   └── filter
│       │   │   │       └── default.js
│       │   │   ├── pastefromword
│       │   │   │   └── filter
│       │   │   │       └── default.js
│       │   │   ├── pastetools
│       │   │   │   └── filter
│       │   │   │       ├── common.js
│       │   │   │       └── image.js
│       │   │   ├── placeholder
│       │   │   │   ├── dialogs
│       │   │   │   │   └── placeholder.js
│       │   │   │   ├── icons
│       │   │   │   │   ├── hidpi
│       │   │   │   │   │   └── placeholder.png
│       │   │   │   │   └── placeholder.png
│       │   │   │   ├── lang
│       │   │   │   │   ├── af.js
│       │   │   │   │   ├── ar.js
│       │   │   │   │   ├── bg.js
│       │   │   │   │   ├── ca.js
│       │   │   │   │   ├── cs.js
│       │   │   │   │   ├── cy.js
│       │   │   │   │   ├── da.js
│       │   │   │   │   ├── de.js
│       │   │   │   │   ├── el.js
│       │   │   │   │   ├── en-gb.js
│       │   │   │   │   ├── en.js
│       │   │   │   │   ├── eo.js
│       │   │   │   │   ├── es.js
│       │   │   │   │   ├── et.js
│       │   │   │   │   ├── eu.js
│       │   │   │   │   ├── fa.js
│       │   │   │   │   ├── fi.js
│       │   │   │   │   ├── fr-ca.js
│       │   │   │   │   ├── fr.js
│       │   │   │   │   ├── gl.js
│       │   │   │   │   ├── he.js
│       │   │   │   │   ├── hr.js
│       │   │   │   │   ├── hu.js
│       │   │   │   │   ├── id.js
│       │   │   │   │   ├── it.js
│       │   │   │   │   ├── ja.js
│       │   │   │   │   ├── km.js
│       │   │   │   │   ├── ko.js
│       │   │   │   │   ├── ku.js
│       │   │   │   │   ├── lv.js
│       │   │   │   │   ├── nb.js
│       │   │   │   │   ├── nl.js
│       │   │   │   │   ├── no.js
│       │   │   │   │   ├── pl.js
│       │   │   │   │   ├── pt-br.js
│       │   │   │   │   ├── pt.js
│       │   │   │   │   ├── ru.js
│       │   │   │   │   ├── si.js
│       │   │   │   │   ├── sk.js
│       │   │   │   │   ├── sl.js
│       │   │   │   │   ├── sq.js
│       │   │   │   │   ├── sv.js
│       │   │   │   │   ├── th.js
│       │   │   │   │   ├── tr.js
│       │   │   │   │   ├── tt.js
│       │   │   │   │   ├── ug.js
│       │   │   │   │   ├── uk.js
│       │   │   │   │   ├── vi.js
│       │   │   │   │   ├── zh-cn.js
│       │   │   │   │   └── zh.js
│       │   │   │   └── plugin.js
│       │   │   ├── preview
│       │   │   │   ├── images
│       │   │   │   │   └── pagebreak.gif
│       │   │   │   ├── styles
│       │   │   │   │   └── screen.css
│       │   │   │   └── preview.html
│       │   │   ├── scayt
│       │   │   │   ├── dialogs
│       │   │   │   │   ├── dialog.css
│       │   │   │   │   ├── options.js
│       │   │   │   │   └── toolbar.css
│       │   │   │   ├── skins
│       │   │   │   │   └── moono-lisa
│       │   │   │   │       └── scayt.css
│       │   │   │   ├── CHANGELOG.md
│       │   │   │   ├── LICENSE.md
│       │   │   │   └── README.md
│       │   │   ├── sharedspace
│       │   │   │   └── plugin.js
│       │   │   ├── showblocks
│       │   │   │   └── images
│       │   │   │       ├── block_address.png
│       │   │   │       ├── block_blockquote.png
│       │   │   │       ├── block_div.png
│       │   │   │       ├── block_h1.png
│       │   │   │       ├── block_h2.png
│       │   │   │       ├── block_h3.png
│       │   │   │       ├── block_h4.png
│       │   │   │       ├── block_h5.png
│       │   │   │       ├── block_h6.png
│       │   │   │       ├── block_p.png
│       │   │   │       └── block_pre.png
│       │   │   ├── smiley
│       │   │   │   ├── dialogs
│       │   │   │   │   └── smiley.js
│       │   │   │   └── images
│       │   │   │       ├── angel_smile.gif
│       │   │   │       ├── angel_smile.png
│       │   │   │       ├── angry_smile.gif
│       │   │   │       ├── angry_smile.png
│       │   │   │       ├── broken_heart.gif
│       │   │   │       ├── broken_heart.png
│       │   │   │       ├── confused_smile.gif
│       │   │   │       ├── confused_smile.png
│       │   │   │       ├── cry_smile.gif
│       │   │   │       ├── cry_smile.png
│       │   │   │       ├── devil_smile.gif
│       │   │   │       ├── devil_smile.png
│       │   │   │       ├── embaressed_smile.gif
│       │   │   │       ├── embarrassed_smile.gif
│       │   │   │       ├── embarrassed_smile.png
│       │   │   │       ├── envelope.gif
│       │   │   │       ├── envelope.png
│       │   │   │       ├── heart.gif
│       │   │   │       ├── heart.png
│       │   │   │       ├── kiss.gif
│       │   │   │       ├── kiss.png
│       │   │   │       ├── lightbulb.gif
│       │   │   │       ├── lightbulb.png
│       │   │   │       ├── omg_smile.gif
│       │   │   │       ├── omg_smile.png
│       │   │   │       ├── regular_smile.gif
│       │   │   │       ├── regular_smile.png
│       │   │   │       ├── sad_smile.gif
│       │   │   │       ├── sad_smile.png
│       │   │   │       ├── shades_smile.gif
│       │   │   │       ├── shades_smile.png
│       │   │   │       ├── teeth_smile.gif
│       │   │   │       ├── teeth_smile.png
│       │   │   │       ├── thumbs_down.gif
│       │   │   │       ├── thumbs_down.png
│       │   │   │       ├── thumbs_up.gif
│       │   │   │       ├── thumbs_up.png
│       │   │   │       ├── tongue_smile.gif
│       │   │   │       ├── tongue_smile.png
│       │   │   │       ├── tounge_smile.gif
│       │   │   │       ├── whatchutalkingabout_smile.gif
│       │   │   │       ├── whatchutalkingabout_smile.png
│       │   │   │       ├── wink_smile.gif
│       │   │   │       └── wink_smile.png
│       │   │   ├── sourcedialog
│       │   │   │   ├── dialogs
│       │   │   │   │   └── sourcedialog.js
│       │   │   │   ├── icons
│       │   │   │   │   ├── hidpi
│       │   │   │   │   │   ├── sourcedialog-rtl.png
│       │   │   │   │   │   └── sourcedialog.png
│       │   │   │   │   ├── sourcedialog-rtl.png
│       │   │   │   │   └── sourcedialog.png
│       │   │   │   ├── lang
│       │   │   │   │   ├── af.js
│       │   │   │   │   ├── ar.js
│       │   │   │   │   ├── bg.js
│       │   │   │   │   ├── bn.js
│       │   │   │   │   ├── bs.js
│       │   │   │   │   ├── ca.js
│       │   │   │   │   ├── cs.js
│       │   │   │   │   ├── cy.js
│       │   │   │   │   ├── da.js
│       │   │   │   │   ├── de.js
│       │   │   │   │   ├── el.js
│       │   │   │   │   ├── en-au.js
│       │   │   │   │   ├── en-ca.js
│       │   │   │   │   ├── en-gb.js
│       │   │   │   │   ├── en.js
│       │   │   │   │   ├── eo.js
│       │   │   │   │   ├── es.js
│       │   │   │   │   ├── et.js
│       │   │   │   │   ├── eu.js
│       │   │   │   │   ├── fa.js
│       │   │   │   │   ├── fi.js
│       │   │   │   │   ├── fo.js
│       │   │   │   │   ├── fr-ca.js
│       │   │   │   │   ├── fr.js
│       │   │   │   │   ├── gl.js
│       │   │   │   │   ├── gu.js
│       │   │   │   │   ├── he.js
│       │   │   │   │   ├── hi.js
│       │   │   │   │   ├── hr.js
│       │   │   │   │   ├── hu.js
│       │   │   │   │   ├── id.js
│       │   │   │   │   ├── is.js
│       │   │   │   │   ├── it.js
│       │   │   │   │   ├── ja.js
│       │   │   │   │   ├── ka.js
│       │   │   │   │   ├── km.js
│       │   │   │   │   ├── ko.js
│       │   │   │   │   ├── ku.js
│       │   │   │   │   ├── lt.js
│       │   │   │   │   ├── lv.js
│       │   │   │   │   ├── mn.js
│       │   │   │   │   ├── ms.js
│       │   │   │   │   ├── nb.js
│       │   │   │   │   ├── nl.js
│       │   │   │   │   ├── no.js
│       │   │   │   │   ├── pl.js
│       │   │   │   │   ├── pt-br.js
│       │   │   │   │   ├── pt.js
│       │   │   │   │   ├── ro.js
│       │   │   │   │   ├── ru.js
│       │   │   │   │   ├── si.js
│       │   │   │   │   ├── sk.js
│       │   │   │   │   ├── sl.js
│       │   │   │   │   ├── sq.js
│       │   │   │   │   ├── sr-latn.js
│       │   │   │   │   ├── sr.js
│       │   │   │   │   ├── sv.js
│       │   │   │   │   ├── th.js
│       │   │   │   │   ├── tr.js
│       │   │   │   │   ├── tt.js
│       │   │   │   │   ├── ug.js
│       │   │   │   │   ├── uk.js
│       │   │   │   │   ├── vi.js
│       │   │   │   │   ├── zh-cn.js
│       │   │   │   │   └── zh.js
│       │   │   │   └── plugin.js
│       │   │   ├── specialchar
│       │   │   │   └── dialogs
│       │   │   │       ├── lang
│       │   │   │       │   ├── _translationstatus.txt
│       │   │   │       │   ├── af.js
│       │   │   │       │   ├── ar.js
│       │   │   │       │   ├── az.js
│       │   │   │       │   ├── bg.js
│       │   │   │       │   ├── ca.js
│       │   │   │       │   ├── cs.js
│       │   │   │       │   ├── cy.js
│       │   │   │       │   ├── da.js
│       │   │   │       │   ├── de-ch.js
│       │   │   │       │   ├── de.js
│       │   │   │       │   ├── el.js
│       │   │   │       │   ├── en-au.js
│       │   │   │       │   ├── en-ca.js
│       │   │   │       │   ├── en-gb.js
│       │   │   │       │   ├── en.js
│       │   │   │       │   ├── eo.js
│       │   │   │       │   ├── es-mx.js
│       │   │   │       │   ├── es.js
│       │   │   │       │   ├── et.js
│       │   │   │       │   ├── eu.js
│       │   │   │       │   ├── fa.js
│       │   │   │       │   ├── fi.js
│       │   │   │       │   ├── fr-ca.js
│       │   │   │       │   ├── fr.js
│       │   │   │       │   ├── gl.js
│       │   │   │       │   ├── he.js
│       │   │   │       │   ├── hr.js
│       │   │   │       │   ├── hu.js
│       │   │   │       │   ├── id.js
│       │   │   │       │   ├── it.js
│       │   │   │       │   ├── ja.js
│       │   │   │       │   ├── km.js
│       │   │   │       │   ├── ko.js
│       │   │   │       │   ├── ku.js
│       │   │   │       │   ├── lt.js
│       │   │   │       │   ├── lv.js
│       │   │   │       │   ├── nb.js
│       │   │   │       │   ├── nl.js
│       │   │   │       │   ├── no.js
│       │   │   │       │   ├── oc.js
│       │   │   │       │   ├── pl.js
│       │   │   │       │   ├── pt-br.js
│       │   │   │       │   ├── pt.js
│       │   │   │       │   ├── ro.js
│       │   │   │       │   ├── ru.js
│       │   │   │       │   ├── si.js
│       │   │   │       │   ├── sk.js
│       │   │   │       │   ├── sl.js
│       │   │   │       │   ├── sq.js
│       │   │   │       │   ├── sr-latn.js
│       │   │   │       │   ├── sr.js
│       │   │   │       │   ├── sv.js
│       │   │   │       │   ├── th.js
│       │   │   │       │   ├── tr.js
│       │   │   │       │   ├── tt.js
│       │   │   │       │   ├── ug.js
│       │   │   │       │   ├── uk.js
│       │   │   │       │   ├── vi.js
│       │   │   │       │   ├── zh-cn.js
│       │   │   │       │   └── zh.js
│       │   │   │       └── specialchar.js
│       │   │   ├── stylesheetparser
│       │   │   │   └── plugin.js
│       │   │   ├── table
│       │   │   │   └── dialogs
│       │   │   │       └── table.js
│       │   │   ├── tableresize
│       │   │   │   └── plugin.js
│       │   │   ├── tableselection
│       │   │   │   └── styles
│       │   │   │       └── tableselection.css
│       │   │   ├── tabletools
│       │   │   │   └── dialogs
│       │   │   │       └── tableCell.js
│       │   │   ├── templates
│       │   │   │   ├── dialogs
│       │   │   │   │   ├── templates.css
│       │   │   │   │   └── templates.js
│       │   │   │   ├── templates
│       │   │   │   │   ├── images
│       │   │   │   │   │   ├── template1.gif
│       │   │   │   │   │   ├── template2.gif
│       │   │   │   │   │   └── template3.gif
│       │   │   │   │   └── default.js
│       │   │   │   └── templatedefinition.js
│       │   │   ├── uicolor
│       │   │   │   ├── dialogs
│       │   │   │   │   └── uicolor.js
│       │   │   │   ├── icons
│       │   │   │   │   ├── hidpi
│       │   │   │   │   │   └── uicolor.png
│       │   │   │   │   └── uicolor.png
│       │   │   │   ├── lang
│       │   │   │   │   ├── _translationstatus.txt
│       │   │   │   │   ├── af.js
│       │   │   │   │   ├── ar.js
│       │   │   │   │   ├── bg.js
│       │   │   │   │   ├── ca.js
│       │   │   │   │   ├── cs.js
│       │   │   │   │   ├── cy.js
│       │   │   │   │   ├── da.js
│       │   │   │   │   ├── de.js
│       │   │   │   │   ├── el.js
│       │   │   │   │   ├── en-gb.js
│       │   │   │   │   ├── en.js
│       │   │   │   │   ├── eo.js
│       │   │   │   │   ├── es.js
│       │   │   │   │   ├── et.js
│       │   │   │   │   ├── eu.js
│       │   │   │   │   ├── fa.js
│       │   │   │   │   ├── fi.js
│       │   │   │   │   ├── fr-ca.js
│       │   │   │   │   ├── fr.js
│       │   │   │   │   ├── gl.js
│       │   │   │   │   ├── he.js
│       │   │   │   │   ├── hr.js
│       │   │   │   │   ├── hu.js
│       │   │   │   │   ├── id.js
│       │   │   │   │   ├── it.js
│       │   │   │   │   ├── ja.js
│       │   │   │   │   ├── km.js
│       │   │   │   │   ├── ko.js
│       │   │   │   │   ├── ku.js
│       │   │   │   │   ├── lv.js
│       │   │   │   │   ├── mk.js
│       │   │   │   │   ├── nb.js
│       │   │   │   │   ├── nl.js
│       │   │   │   │   ├── no.js
│       │   │   │   │   ├── pl.js
│       │   │   │   │   ├── pt-br.js
│       │   │   │   │   ├── pt.js
│       │   │   │   │   ├── ru.js
│       │   │   │   │   ├── si.js
│       │   │   │   │   ├── sk.js
│       │   │   │   │   ├── sl.js
│       │   │   │   │   ├── sq.js
│       │   │   │   │   ├── sv.js
│       │   │   │   │   ├── tr.js
│       │   │   │   │   ├── tt.js
│       │   │   │   │   ├── ug.js
│       │   │   │   │   ├── uk.js
│       │   │   │   │   ├── vi.js
│       │   │   │   │   ├── zh-cn.js
│       │   │   │   │   └── zh.js
│       │   │   │   ├── yui
│       │   │   │   │   ├── assets
│       │   │   │   │   │   ├── hue_bg.png
│       │   │   │   │   │   ├── hue_thumb.png
│       │   │   │   │   │   ├── picker_mask.png
│       │   │   │   │   │   ├── picker_thumb.png
│       │   │   │   │   │   └── yui.css
│       │   │   │   │   └── yui.js
│       │   │   │   └── plugin.js
│       │   │   ├── uploadimage
│       │   │   │   └── plugin.js
│       │   │   ├── uploadwidget
│       │   │   │   ├── lang
│       │   │   │   │   ├── cs.js
│       │   │   │   │   ├── da.js
│       │   │   │   │   ├── de.js
│       │   │   │   │   ├── en.js
│       │   │   │   │   ├── eo.js
│       │   │   │   │   ├── fr.js
│       │   │   │   │   ├── gl.js
│       │   │   │   │   ├── hu.js
│       │   │   │   │   ├── it.js
│       │   │   │   │   ├── ko.js
│       │   │   │   │   ├── ku.js
│       │   │   │   │   ├── nb.js
│       │   │   │   │   ├── nl.js
│       │   │   │   │   ├── pl.js
│       │   │   │   │   ├── pt-br.js
│       │   │   │   │   ├── ru.js
│       │   │   │   │   ├── sv.js
│       │   │   │   │   ├── tr.js
│       │   │   │   │   ├── zh-cn.js
│       │   │   │   │   └── zh.js
│       │   │   │   └── plugin.js
│       │   │   ├── widget
│       │   │   │   ├── images
│       │   │   │   │   └── handle.png
│       │   │   │   ├── lang
│       │   │   │   │   ├── af.js
│       │   │   │   │   ├── ar.js
│       │   │   │   │   ├── bg.js
│       │   │   │   │   ├── ca.js
│       │   │   │   │   ├── cs.js
│       │   │   │   │   ├── cy.js
│       │   │   │   │   ├── da.js
│       │   │   │   │   ├── de.js
│       │   │   │   │   ├── el.js
│       │   │   │   │   ├── en-gb.js
│       │   │   │   │   ├── en.js
│       │   │   │   │   ├── eo.js
│       │   │   │   │   ├── es.js
│       │   │   │   │   ├── fa.js
│       │   │   │   │   ├── fi.js
│       │   │   │   │   ├── fr.js
│       │   │   │   │   ├── gl.js
│       │   │   │   │   ├── he.js
│       │   │   │   │   ├── hr.js
│       │   │   │   │   ├── hu.js
│       │   │   │   │   ├── it.js
│       │   │   │   │   ├── ja.js
│       │   │   │   │   ├── km.js
│       │   │   │   │   ├── ko.js
│       │   │   │   │   ├── ku.js
│       │   │   │   │   ├── lv.js
│       │   │   │   │   ├── nb.js
│       │   │   │   │   ├── nl.js
│       │   │   │   │   ├── no.js
│       │   │   │   │   ├── pl.js
│       │   │   │   │   ├── pt-br.js
│       │   │   │   │   ├── pt.js
│       │   │   │   │   ├── ru.js
│       │   │   │   │   ├── sk.js
│       │   │   │   │   ├── sl.js
│       │   │   │   │   ├── sq.js
│       │   │   │   │   ├── sv.js
│       │   │   │   │   ├── tr.js
│       │   │   │   │   ├── tt.js
│       │   │   │   │   ├── uk.js
│       │   │   │   │   ├── vi.js
│       │   │   │   │   ├── zh-cn.js
│       │   │   │   │   └── zh.js
│       │   │   │   └── plugin.js
│       │   │   ├── wsc
│       │   │   │   ├── dialogs
│       │   │   │   │   ├── ciframe.html
│       │   │   │   │   ├── tmpFrameset.html
│       │   │   │   │   ├── wsc.css
│       │   │   │   │   ├── wsc.js
│       │   │   │   │   └── wsc_ie.js
│       │   │   │   ├── icons
│       │   │   │   │   ├── hidpi
│       │   │   │   │   │   └── spellchecker.png
│       │   │   │   │   └── spellchecker.png
│       │   │   │   ├── lang
│       │   │   │   │   ├── af.js
│       │   │   │   │   ├── ar.js
│       │   │   │   │   ├── bg.js
│       │   │   │   │   ├── bn.js
│       │   │   │   │   ├── bs.js
│       │   │   │   │   ├── ca.js
│       │   │   │   │   ├── cs.js
│       │   │   │   │   ├── cy.js
│       │   │   │   │   ├── da.js
│       │   │   │   │   ├── de.js
│       │   │   │   │   ├── el.js
│       │   │   │   │   ├── en-au.js
│       │   │   │   │   ├── en-ca.js
│       │   │   │   │   ├── en-gb.js
│       │   │   │   │   ├── en.js
│       │   │   │   │   ├── eo.js
│       │   │   │   │   ├── es.js
│       │   │   │   │   ├── et.js
│       │   │   │   │   ├── eu.js
│       │   │   │   │   ├── fa.js
│       │   │   │   │   ├── fi.js
│       │   │   │   │   ├── fo.js
│       │   │   │   │   ├── fr-ca.js
│       │   │   │   │   ├── fr.js
│       │   │   │   │   ├── gl.js
│       │   │   │   │   ├── gu.js
│       │   │   │   │   ├── he.js
│       │   │   │   │   ├── hi.js
│       │   │   │   │   ├── hr.js
│       │   │   │   │   ├── hu.js
│       │   │   │   │   ├── is.js
│       │   │   │   │   ├── it.js
│       │   │   │   │   ├── ja.js
│       │   │   │   │   ├── ka.js
│       │   │   │   │   ├── km.js
│       │   │   │   │   ├── ko.js
│       │   │   │   │   ├── ku.js
│       │   │   │   │   ├── lt.js
│       │   │   │   │   ├── lv.js
│       │   │   │   │   ├── mk.js
│       │   │   │   │   ├── mn.js
│       │   │   │   │   ├── ms.js
│       │   │   │   │   ├── nb.js
│       │   │   │   │   ├── nl.js
│       │   │   │   │   ├── no.js
│       │   │   │   │   ├── pl.js
│       │   │   │   │   ├── pt-br.js
│       │   │   │   │   ├── pt.js
│       │   │   │   │   ├── ro.js
│       │   │   │   │   ├── ru.js
│       │   │   │   │   ├── sk.js
│       │   │   │   │   ├── sl.js
│       │   │   │   │   ├── sr-latn.js
│       │   │   │   │   ├── sr.js
│       │   │   │   │   ├── sv.js
│       │   │   │   │   ├── th.js
│       │   │   │   │   ├── tr.js
│       │   │   │   │   ├── ug.js
│       │   │   │   │   ├── uk.js
│       │   │   │   │   ├── vi.js
│       │   │   │   │   ├── zh-cn.js
│       │   │   │   │   └── zh.js
│       │   │   │   ├── skins
│       │   │   │   │   └── moono-lisa
│       │   │   │   │       └── wsc.css
│       │   │   │   ├── LICENSE.md
│       │   │   │   ├── README.md
│       │   │   │   └── plugin.js
│       │   │   ├── xml
│       │   │   │   └── plugin.js
│       │   │   ├── icons.png
│       │   │   └── icons_hidpi.png
│       │   ├── skins
│       │   │   ├── moono
│       │   │   │   ├── images
│       │   │   │   │   ├── hidpi
│       │   │   │   │   │   ├── close.png
│       │   │   │   │   │   ├── lock-open.png
│       │   │   │   │   │   ├── lock.png
│       │   │   │   │   │   └── refresh.png
│       │   │   │   │   ├── arrow.png
│       │   │   │   │   ├── close.png
│       │   │   │   │   ├── lock-open.png
│       │   │   │   │   ├── lock.png
│       │   │   │   │   ├── refresh.png
│       │   │   │   │   └── spinner.gif
│       │   │   │   ├── dialog.css
│       │   │   │   ├── dialog_ie.css
│       │   │   │   ├── dialog_ie7.css
│       │   │   │   ├── dialog_ie8.css
│       │   │   │   ├── dialog_iequirks.css
│       │   │   │   ├── editor.css
│       │   │   │   ├── editor_gecko.css
│       │   │   │   ├── editor_ie.css
│       │   │   │   ├── editor_ie7.css
│       │   │   │   ├── editor_ie8.css
│       │   │   │   ├── editor_iequirks.css
│       │   │   │   ├── icons.png
│       │   │   │   ├── icons_hidpi.png
│       │   │   │   └── readme.md
│       │   │   └── moono-lisa
│       │   │       ├── images
│       │   │       │   ├── hidpi
│       │   │       │   │   ├── close.png
│       │   │       │   │   ├── lock-open.png
│       │   │       │   │   ├── lock.png
│       │   │       │   │   └── refresh.png
│       │   │       │   ├── arrow.png
│       │   │       │   ├── close.png
│       │   │       │   ├── lock-open.png
│       │   │       │   ├── lock.png
│       │   │       │   ├── refresh.png
│       │   │       │   └── spinner.gif
│       │   │       ├── dialog.css
│       │   │       ├── dialog_ie.css
│       │   │       ├── dialog_ie8.css
│       │   │       ├── dialog_iequirks.css
│       │   │       ├── editor.css
│       │   │       ├── editor_gecko.css
│       │   │       ├── editor_ie.css
│       │   │       ├── editor_ie8.css
│       │   │       ├── editor_iequirks.css
│       │   │       ├── icons.png
│       │   │       ├── icons_hidpi.png
│       │   │       └── readme.md
│       │   ├── vendor
│       │   │   └── promise.js
│       │   ├── CHANGES.md
│       │   ├── LICENSE.md
│       │   ├── README.md
│       │   ├── SECURITY.md
│       │   ├── bender-runner.config.json
│       │   ├── build-config.js
│       │   ├── ckeditor.js
│       │   ├── config.js
│       │   ├── contents.css
│       │   └── styles.js
│       ├── ckeditor_uploader
│       │   └── admin_base.css
│       ├── file-icons
│       │   ├── doc.png
│       │   ├── file.png
│       │   ├── pdf.png
│       │   ├── ppt.png
│       │   ├── swf.png
│       │   ├── txt.png
│       │   └── xls.png
│       ├── galleriffic
│       │   ├── css
│       │   │   ├── basic.css
│       │   │   ├── black.css
│       │   │   ├── caption.png
│       │   │   ├── galleriffic-1.css
│       │   │   ├── galleriffic-2.css
│       │   │   ├── galleriffic-3.css
│       │   │   ├── galleriffic-4.css
│       │   │   ├── galleriffic-5.css
│       │   │   ├── jush.css
│       │   │   ├── loader.gif
│       │   │   ├── loaderWhite.gif
│       │   │   ├── nextPageArrow.gif
│       │   │   ├── nextPageArrowWhite.gif
│       │   │   ├── prevPageArrow.gif
│       │   │   ├── prevPageArrowWhite.gif
│       │   │   └── white.css
│       │   └── js
│       │       ├── jquery-1.3.2.js
│       │       ├── jquery.galleriffic.js
│       │       ├── jquery.history.js
│       │       ├── jquery.opacityrollover.js
│       │       └── jush.js
│       ├── ckeditor-init.js
│       ├── ckeditor.css
│       └── fixups.js
├── Projeto Transbirday.docx
├── comandos bash.txt
├── db.sqlite3
├── file tree.md
├── manage.py
└── requirements.txt
```

---
*Generated by FileTree Pro Extension*