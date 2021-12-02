(this["webpackJsonp4103-table"]=this["webpackJsonp4103-table"]||[]).push([[0],{106:function(e,t,r){},139:function(e,t,r){"use strict";r.r(t);var s=r(0),n=r.n(s),c=r(14),a=r.n(c),o=(r(83),r(11)),i=r.n(o),l=r(24),u=r(4),d=r(12),j=(r(44),r(77)),h=r(146),p=r(150),b=r(147),O=r(73),m=r(148),g=r(23),f=r.n(g),x=(r(65),r(1));function S(){var e=Object(s.useState)([]),t=Object(u.a)(e,2),r=t[0],n=t[1],c=Object(s.useState)({cohortList:[],semesterList:[],cohortDropdowns:[],semesterDropdowns:[]}),a=Object(u.a)(c,2),o=a[0],i=a[1],l=Object(s.useState)({title:"",input:""}),g=Object(u.a)(l,2),S=g[0],C=g[1],v=Object(s.useState)({coop:0,total:0,FIR:0,SOP:0,JUN:0,SEN:0}),_=Object(u.a)(v,2),E=_[0],y=_[1];return Object(s.useEffect)((function(){var e="",t=0,r=window.location.hostname;"localhost"===r||"127.0.0.1"===r?"cohort"===S.title.toLowerCase()?e="http://"+r+":8000/api/counts_cohort/"+S.input:(e="http://"+r+":8000/api/counts_semester/"+S.input,t=1):"cohort"===S.title.toLowerCase()?e="http://"+r+"/api/counts_cohort/"+S.input:(e="http://"+r+"/api/counts_semester/"+S.input,t=1),[/\d{4}-\d{4}$/,/\d{4}\/FA|WI|SM$/][t].test(S.input)&&f.a.get(e).then((function(e){y({coop:e.data.countCoop,total:e.data.countTotal,FIR:e.data.FIR,SOP:e.data.SOP,JUN:e.data.JUN,SEN:e.data.SEN})}))}),[S]),Object(s.useEffect)((function(){var e=window.location.hostname;"localhost"===e||"127.0.0.1"===e?f.a.get("http://"+e+":8000/api/count_parameters").then((function(e){var t,r=[],s=Object(d.a)(e.data.cohorts);try{for(s.s();!(t=s.n()).done;){var c=t.value;r.push(Object(x.jsx)(j.a.Item,{eventKey:c,children:c}))}}catch(h){s.e(h)}finally{s.f()}var a,o=[],l=Object(d.a)(e.data.semesters);try{for(l.s();!(a=l.n()).done;){var u=a.value;o.push(Object(x.jsx)(j.a.Item,{eventKey:u,children:u}))}}catch(h){l.e(h)}finally{l.f()}i({cohortList:e.data.cohorts,semesterList:e.data.semesters,cohortDropdowns:r,semesterDropdowns:o}),C({title:"Cohort",input:e.data.cohorts[0]}),n(r)})):f.a.get("http://"+e+"/api/count_parameters").then((function(e){var t,r=[],s=Object(d.a)(e.data.cohorts);try{for(s.s();!(t=s.n()).done;){var c=t.value;r.push(Object(x.jsx)(j.a.Item,{eventKey:c,children:c}))}}catch(h){s.e(h)}finally{s.f()}var a,o=[],l=Object(d.a)(e.data.semesters);try{for(l.s();!(a=l.n()).done;){var u=a.value;o.push(Object(x.jsx)(j.a.Item,{eventKey:u,children:u}))}}catch(h){l.e(h)}finally{l.f()}i({cohortList:e.data.cohorts,semesterList:e.data.semesters,cohortDropdowns:r,semesterDropdowns:o}),C({title:"Cohort",input:e.data.cohorts[0]}),n(r)}))}),[]),Object(x.jsxs)("div",{className:"countsCard",children:[Object(x.jsxs)("div",{className:"headerDiv",children:[Object(x.jsx)("div",{className:"dropdownDiv",children:Object(x.jsxs)(h.a,{id:"dropdown-basic-button",title:S.title,variant:"danger",onSelect:function(e){"cohort"===e.toLowerCase()?(n(o.cohortDropdowns),C({title:e,input:o.cohortList[0]})):(n(o.semesterDropdowns),C({title:e,input:o.semesterList[0]}))},children:[Object(x.jsx)(j.a.Item,{eventKey:"Cohort",children:"Cohort"}),Object(x.jsx)(j.a.Item,{eventKey:"Semester",children:"Semester"})]})}),Object(x.jsx)("div",{className:"formDiv",children:Object(x.jsx)(p.a,{children:Object(x.jsx)(b.a,{children:Object(x.jsx)(O.a,{children:Object(x.jsx)(h.a,{id:"dropdown-basic-button",title:S.input,variant:"danger",onSelect:function(e){return C({title:S.title,input:e})},children:r})})})})})]}),Object(x.jsx)("div",{className:"tableDiv",children:Object(x.jsxs)(m.a,{hover:!0,size:"sm",children:[Object(x.jsx)("thead",{children:Object(x.jsxs)("tr",{children:[Object(x.jsx)("th",{}),Object(x.jsx)("th",{children:"Count"})]})}),Object(x.jsxs)("tbody",{className:"counts_tbody",children:[Object(x.jsxs)("tr",{children:[Object(x.jsx)("td",{children:"Total"}),Object(x.jsx)("td",{children:E.total})]}),Object(x.jsxs)("tr",{children:[Object(x.jsx)("td",{children:"Coop"}),Object(x.jsx)("td",{children:E.coop})]}),Object(x.jsxs)("tr",{children:[Object(x.jsx)("td",{children:"FIR"}),Object(x.jsx)("td",{children:E.FIR})]}),Object(x.jsxs)("tr",{children:[Object(x.jsx)("td",{children:"SOP"}),Object(x.jsx)("td",{children:E.SOP})]}),Object(x.jsxs)("tr",{children:[Object(x.jsx)("td",{children:"JUN"}),Object(x.jsx)("td",{children:E.JUN})]}),Object(x.jsxs)("tr",{children:[Object(x.jsx)("td",{children:"SEN"}),Object(x.jsx)("td",{children:E.SEN})]})]})]})})]})}var C=r(71);function v(e){var t=e.checked,r={},n=Object(s.useState)(!1),c=Object(u.a)(n,2),a=c[0],o=c[1],j=function(){var e=Object(l.a)(i.a.mark((function e(t){var r,s,n;return i.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return r=window.location.hostname,s="localhost"===r||"127.0.0.1"===r?"http://"+r+":8000/audit_student/"+t:"http://swe4103-env.eba-irrkpdyi.us-east-2.elasticbeanstalk.com/_get_Audit/"+t,e.next=4,f.a.get(s);case 4:return n=e.sent,e.abrupt("return",n.data);case 6:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),h=function(e){var t=[],r=e.target_student,s={CORE:e.progress.CORE,TE:e.progress.TE,NS:e.progress.NS,CSE:{ITS:e.progress["CSE-ITS"],HSS:e.progress["CSE-HSS"],OPEN:e.progress["CSE-OPEN"]}},n=["Audit: ",r.student_number," - ",r.full_name,", ",r.cohort,", ",r.rank,", years in: ",r.years_in,"\nBased on: ",e.base_program," program, as of ",e.latest_enrolment_term,"\n\n\tSTATUS: ",r.status];t=t.concat(n);for(var c=0,a=Object.entries(s);c<a.length;c++){var o=Object(u.a)(a[c],2),i=o[0],l=o[1];if("CSE"===i)break;var j=l.completed.courses,h=l.completed.credit_hours,p="CORE"===i?l.remaining.courses:l.remaining.num_courses,b=l.remaining.credit_hours,O=l.in_progress.courses,m=l.in_progress.credit_hours,g=["\n\n==========================================================================\n","Progress through ",i," (","CORE"===i?j.length+p.length+O.length:j.length+p+O.length," courses, ",h+b+m," CH)    ",("CORE"===i?p.length:p).toString()," courses (",b.toString(),"CH) REMAINING\n","==========================================================================\n"];t=t.concat(g),t="CORE"===i?t.concat(["()** indicates equivelent course replacement\n\n"]):t.concat(["\n"]);for(var f=[i," courses completed:    ",j.length.toString()," courses (",h.toString(),"CH)\n","---------------------------------------------\n"],x=0;x<j.length;++x)f=x>1&&x%5===0?f.concat([j[x],"\n"]):f.concat([j[x],", "]);f=f.concat(["\n\n"]),t=t.concat(f);for(var S=[i," courses in progress:    ",O.length.toString()," courses (",m.toString(),"CH)\n","---------------------------------------------\n"],C=0;C<O.length;++C)S=C>1&&C%5===0?S.concat([O[C],"\n"]):S.concat([O[C],", "]);if(S=S.concat(["\n\n"]),t=t.concat(S),"CORE"===i){for(var v=[i," courses remaining:    ",p.length.toString()," courses (",b.toString(),"CH)\n","---------------------------------------------\n"],_=0;_<p.length;++_)v=_>1&&_%5===0?v.concat([p[_],"\n"]):v.concat([p[_],", "]);v=v.concat(["\n\n"]),t=t.concat(v)}}var E=s.CSE,y=E.ITS.completed.courses.length+E.ITS.remaining.num_courses+E.ITS.in_progress.courses.length,N=E.ITS.completed.credit_hours+E.ITS.remaining.credit_hours+E.ITS.in_progress.credit_hours,T=E.HSS.completed.courses.length+E.HSS.remaining.num_courses+E.HSS.in_progress.courses.length,I=E.HSS.completed.credit_hours+E.HSS.remaining.credit_hours+E.HSS.in_progress.credit_hours,H=E.OPEN.completed.courses.length+E.OPEN.remaining.num_courses+E.OPEN.in_progress.courses.length,w=N+I+(E.OPEN.completed.credit_hours+E.OPEN.remaining.credit_hours+E.OPEN.in_progress.credit_hours),P=E.HSS.remaining.num_courses+E.ITS.remaining.num_courses+E.OPEN.remaining.num_courses,F=E.HSS.remaining.credit_hours+E.ITS.remaining.credit_hours+E.OPEN.remaining.credit_hours,R=["\n\n==========================================================================\n","Progress through CSE (",y.toString()," ITS, ",T.toString()," HSS, ",H.toString()," OPEN; ",w.toString(),"CH)     ",P.toString()," courses (",F.toString(),") REMAINING\n","==========================================================================\n"];t=t.concat(R);for(var k=0,A=Object.entries(E);k<A.length;k++){var D=Object(u.a)(A[k],2),L=D[0],G=D[1],z=G.completed.courses,B=G.in_progress.courses;if(z.length>0){t=t.concat(["CSE-",L," ",z.length.toString()," (",G.completed.credit_hours.toString(),"ch) complete: "]);var M,U=Object(d.a)(z);try{for(U.s();!(M=U.n()).done;){var V=M.value;t=t.concat([V,", "])}}catch(W){U.e(W)}finally{U.f()}t=t.concat(["\n"])}if(B.length>0){t=t.concat(["CSE-",L," ",B.length.toString()," (",G.in_progress.credit_hours.toString(),"ch) inprogress: "]);var J,K=Object(d.a)(B);try{for(K.s();!(J=K.n()).done;){var Y=J.value;t=t.concat([Y,", "])}}catch(W){K.e(W)}finally{K.f()}t=t.concat(["\n"])}}return(t=t.concat(["\n\n"])).join("")};Object(s.useEffect)((function(){if(a){var e,s=[],n=Object(d.a)(t);try{for(n.s();!(e=n.n()).done;){var c=e.value;s.push(j(c))}}catch(i){n.e(i)}finally{n.f()}Promise.all(s).then((function(e){var t,s=Object(d.a)(e);try{for(s.s();!(t=s.n()).done;){var n=t.value;r[n.target_student.student_number]=n}}catch(i){s.e(i)}finally{s.f()}for(var c="",a="",l=0,j=Object.entries(r);l<j.length;l++){var p=Object(u.a)(j[l],2),b=p[0],O=p[1];c+=b+"-",a+=h(O)}(function(e,t){var r=document.createElement("a"),s=new Blob([t],{type:"text/plain"});r.href=URL.createObjectURL(s),r.download=e,document.body.appendChild(r),r.click()})(c+="audit.txt",a),o(!1)}))}}),[t,r,a]);return Object(x.jsx)(x.Fragment,{children:Object(x.jsx)(C.a,{variant:"danger",size:"lg",disabled:a,onClick:a?null:function(){return o(!0)},children:"Generate Text Audit"})})}r(106);function _(e){return E.apply(this,arguments)}function E(){return(E=Object(l.a)(i.a.mark((function e(t){var r,s,n,c,a,o,l,u,d;return i.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if("localhost"!==(r=window.location.hostname)&&"127.0.0.1"!==r){e.next=13;break}return s="http://"+r+":8000/api/student_data",e.next=5,fetch(s);case 5:return n=e.sent,e.next=8,n.json();case 8:return c=e.sent,e.next=11,c.map((function(e){return e.fields}));case 11:return a=e.sent,e.abrupt("return",t(a));case 13:return o="http://"+r+"/api/student_data",e.next=16,fetch(o);case 16:return l=e.sent,e.next=19,l.json();case 19:return u=e.sent,e.next=22,u.map((function(e){return e.fields}));case 22:return d=e.sent,e.abrupt("return",t(d));case 24:case"end":return e.stop()}}),e)})))).apply(this,arguments)}function y(e,t,r){return N.apply(this,arguments)}function N(){return(N=Object(l.a)(i.a.mark((function e(t,r,s){var n,c,a,o,l,u,d;return i.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(n=window.location.hostname,0===t.length){e.next=23;break}if("localhost"!==n&&"127.0.0.1"!==n){e.next=14;break}return c="http://"+n+":8000/get_transcript/"+t[1],e.next=6,fetch(c);case 6:return a=e.sent,e.next=9,a.json();case 9:return o=e.sent,s(!1),e.abrupt("return",r(o));case 14:return l="http://"+n+"/get_transcript/"+t[1],e.next=17,fetch(l);case 17:return u=e.sent,e.next=20,u.json();case 20:return d=e.sent,s(!1),e.abrupt("return",r(d));case 23:case"end":return e.stop()}}),e)})))).apply(this,arguments)}function T(e,t){return I.apply(this,arguments)}function I(){return(I=Object(l.a)(i.a.mark((function e(t,r){var s,n,c,a,o,l;return i.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(s=window.location.hostname,0===t.length){e.next=21;break}if("localhost"!==s&&"127.0.0.1"!==s){e.next=13;break}return n="http://"+s+":8000/audit_student/"+t[1],e.next=6,fetch(n);case 6:return c=e.sent,e.next=9,c.json();case 9:return c=e.sent,e.abrupt("return",r(c));case 13:return a="http://"+s+"/audit_student/"+t[1],e.next=16,f.a.get(a);case 16:return o=e.sent,e.next=19,o.json();case 19:return l=e.sent,e.abrupt("return",r(l));case 21:case"end":return e.stop()}}),e)})))).apply(this,arguments)}var H=r(2),w=r(10),P=r(74);function F(e){var t=e.column,r=t.filterValue,s=t.preFilteredRows,n=t.setFilter;s.length;return Object(x.jsx)("input",{value:r||"",onChange:function(e){n(e.target.value||void 0)},placeholder:"Search Records..."})}function R(e){var t=e.column,r=t.filterValue,s=t.setFilter,c=t.preFilteredRows,a=t.id,o=n.a.useMemo((function(){var e=new Set;return c.forEach((function(t){e.add(t.values[a])})),Object(w.a)(e.values())}),[a,c]);return Object(x.jsxs)("select",{value:r,onChange:function(e){s(e.target.value||void 0)},children:[Object(x.jsx)("option",{value:"",children:"All"}),o.map((function(e,t){return Object(x.jsx)("option",{value:e,children:e},t)}))]})}function k(e,t,r){return Object(P.a)(e,r,{keys:[function(e){return e.values[t]}]})}var A=r(18),D=r(3),L=["indeterminate"],G=n.a.forwardRef((function(e,t){var r=e.indeterminate,s=Object(D.a)(e,L),c=n.a.useRef(),a=t||c;return n.a.useEffect((function(){a.current.indeterminate=r}),[a,r]),Object(x.jsx)(x.Fragment,{children:Object(x.jsx)("input",Object(H.a)({type:"checkbox",ref:a},s))})}));function z(e){var t=e.columns,r=e.data,s=(e.modalClose,e.modalOpen),c=(e.modalState,e.selectKey),a=e.selectRow,o=e.updateChecked,i=e.setTranLoad;function l(e,t){if("selection"!==t.column.id){var r=e.cells.map((function(e){if("student_number"===e.column.id)return e.value})),n=e.cells.map((function(e){if("name"===e.column.id)return e.value})),o=e.cells.map((function(e){if("rank"===e.column.id)return e.value})),l=e.cells.map((function(e){if("program"===e.column.id)return e.value})),u=e.cells.map((function(e){if("status"===e.column.id)return e.value})),d=e.cells.map((function(e){if("campus"===e.column.id)return e.value}));i(!0),s(),a({name:n,program:l,campus:d,rank:o,status:u}),c(r)}}var u=n.a.useMemo((function(){return{fuzzyText:k,text:function(e,t,r){return e.filter((function(e){var s=e.values[t];return void 0===s||String(s).toLowerCase().startsWith(String(r).toLowerCase())}))}}}),[]),j=n.a.useMemo((function(){return{Filter:F}}),[]),h=Object(A.useTable)({columns:t,data:r,defaultColumn:j,filterTypes:u},A.useFilters,A.useGlobalFilter,A.useSortBy,A.useRowSelect,(function(e){e.visibleColumns.push((function(e){return[{id:"selection",Header:function(e){var t=e.getToggleAllRowsSelectedProps;return Object(x.jsx)("div",{children:Object(x.jsx)(G,Object(H.a)({},t()))})},Cell:function(e){var t=e.row;return Object(x.jsx)(G,Object(H.a)({},t.getToggleRowSelectedProps()))}}].concat(Object(w.a)(e))}))})),p=h.getTableProps,b=h.getTableBodyProps,O=h.headerGroups,m=h.rows,g=h.prepareRow,f=(h.state,h.selectedFlatRows);h.visibleColumns;n.a.useEffect((function(){var e,t=[],r=Object(d.a)(f);try{for(r.s();!(e=r.n()).done;){e.value.cells.map((function(e){"student_number"===e.column.id&&t.push(e.value)}))}}catch(s){r.e(s)}finally{r.f()}o(t)}),[f]);var S=m;return Object(x.jsxs)(x.Fragment,{children:[Object(x.jsxs)("table",Object(H.a)(Object(H.a)({className:"styled-table"},p()),{},{children:[Object(x.jsx)("thead",{children:O.map((function(e,t){if(t>0)return Object(x.jsx)("tr",Object(H.a)(Object(H.a)({},e.getHeaderGroupProps()),{},{children:e.headers.map((function(e){return Object(x.jsxs)("th",Object(H.a)(Object(H.a)({},e.getHeaderProps(e.getSortByToggleProps())),{},{children:[e.render("Header"),Object(x.jsxs)("div",{children:[e.canFilter?e.render("Filter"):null,Object(x.jsxs)("span",{children:[e.isSorted?e.isSortedDesc?"\ud83d\udd3d":"\ud83d\udd3c":""," "]})]})]}))}))}))}))}),Object(x.jsx)("tbody",Object(H.a)(Object(H.a)({},b()),{},{children:S.map((function(e,t){return g(e),Object(x.jsx)("tr",Object(H.a)(Object(H.a)({className:"List_Row"},e.getRowProps()),{},{children:e.cells.map((function(t){return Object(x.jsx)("td",Object(H.a)(Object(H.a)({onClick:function(){return l(e,t)},className:"table-td-cell"},t.getCellProps()),{},{children:t.render("Cell")}))}))}))}))}))]})),Object(x.jsx)("pre",{children:Object(x.jsxs)("div",{children:[" ",f.map((function(e,t){return g(e),0===t?Object(x.jsxs)(x.Fragment,{children:[Object(x.jsxs)("tr",{children:[Object(x.jsx)("td",{})," ",Object(x.jsx)("td",{style:{padding:"10px"},children:"Student Number"}),Object(x.jsx)("td",{style:{padding:"10px"},children:"Name"}),Object(x.jsx)("td",{style:{padding:"10px"},children:"Program"}),Object(x.jsx)("td",{style:{padding:"10px"},children:"Campus"}),Object(x.jsx)("td",{style:{padding:"10px"},children:"Rank"}),Object(x.jsx)("td",{style:{padding:"10px"},children:"status"})]}),Object(x.jsx)("tr",Object(H.a)(Object(H.a)({style:{padding:"15px"}},e.getRowProps()),{},{children:e.cells.map((function(t){return Object(x.jsx)("td",Object(H.a)(Object(H.a)({onClick:function(){return l(e,t)},style:{padding:"15px"}},t.getCellProps()),{},{children:t.render("Cell")}))}))})),"  "]}):Object(x.jsx)("tr",Object(H.a)(Object(H.a)({style:{padding:"15px"}},e.getRowProps()),{},{children:e.cells.map((function(t){return Object(x.jsx)("td",Object(H.a)(Object(H.a)({onClick:function(){return l(e,t)},style:{padding:"15px"}},t.getCellProps()),{},{children:t.render("Cell")}))}))}))}))]})}),Object(x.jsx)("br",{})]})}k.autoRemove=function(e){return!e};var B=[{Header:" ",columns:[{Header:"Student ID",accessor:"student_number"},{Header:"Name",accessor:"name"},{Header:"Program",accessor:"program"},{Header:"Campus",accessor:"campus",Filter:R,filter:"includes"},{Header:"Rank",accessor:"rank",sortType:function(e,t,r,s){var n=e.values[r],c=t.values[r],a=0,o=0;return"JUN"===n?a=1:"SOP"===n?a=2:"SEN"===n&&(a=3),"JUN"===c?o=1:"SOP"===c?o=2:"SEN"===c&&(o=3),Number.isNaN(a)&&(a=s?Number.NEGATIVE_INFINITY:Number.POSITIVE_INFINITY),Number.isNaN(o)&&(o=s?Number.NEGATIVE_INFINITY:Number.POSITIVE_INFINITY),a>o?1:a<o?-1:0},Filter:R},{Header:"Status",accessor:"status",Filter:R}]}],M=[{Header:" ",columns:[{Header:"Course Code",accessor:"Course_Code",sortType:function(e,t,r,s){var n=e.values[r];n=n.split("*");var c=t.values[r];c=c.split("*");var a=Number.parseFloat(n[1]),o=Number.parseFloat(c[1]);return Number.isNaN(a)&&(a=s?Number.NEGATIVE_INFINITY:Number.POSITIVE_INFINITY),Number.isNaN(o)&&(o=s?Number.NEGATIVE_INFINITY:Number.POSITIVE_INFINITY),a>o?1:a<o?-1:0},disableFilters:!0},{Header:"Course Name",accessor:"Course_Name",disableFilters:!0},{Header:"Course Type",accessor:"Course_Type",disableFilters:!0},{Header:"Semester",accessor:"Semester",disableFilters:!0},{Header:"Section",accessor:"Section",filter:"includes",disableFilters:!0},{Header:"Credit Hours",accessor:"Credit_Hours",disableFilters:!0},{Header:"Grade",accessor:"Grade",disableFilters:!0}]}],U=r(149);function V(e){var t=e.columns,r=e.data,s=(e.modalClose,e.modalOpen,e.modalState,e.selectKey,e.selectName,n.a.useMemo((function(){return{fuzzyText:k,text:function(e,t,r){return e.filter((function(e){var s=e.values[t];return void 0===s||String(s).toLowerCase().startsWith(String(r).toLowerCase())}))}}}),[])),c=Object(A.useTable)({columns:t,data:r,filterTypes:s},A.useFilters,A.useGlobalFilter,A.useSortBy),a=c.getTableProps,o=c.getTableBodyProps,i=c.headerGroups,l=c.rows,u=c.prepareRow,d=(c.state,c.visibleColumns),j=l;return Object(x.jsxs)(x.Fragment,{children:[Object(x.jsxs)(m.a,Object(H.a)(Object(H.a)({className:"styled-transcript"},a()),{},{children:[Object(x.jsxs)("thead",{className:"styled-transcript-thead",children:[i.map((function(e){return Object(x.jsx)("tr",Object(H.a)(Object(H.a)({},e.getHeaderGroupProps()),{},{children:e.headers.map((function(e){return Object(x.jsxs)("th",Object(H.a)(Object(H.a)({className:"transcript_head"},e.getHeaderProps(e.getSortByToggleProps())),{},{children:[e.render("Header"),Object(x.jsxs)("div",{children:[e.canFilter?e.render("Filter"):null,Object(x.jsxs)("span",{children:[e.isSorted?e.isSortedDesc?"\ud83d\udd3d":"\ud83d\udd3c":""," "]})]})]}))}))}))})),Object(x.jsx)("tr",{children:Object(x.jsx)("th",{colSpan:d.length})})]}),Object(x.jsx)("tbody",Object(H.a)(Object(H.a)({className:"styled-transcript-tbody"},o()),{},{children:j.map((function(e,t){return u(e),Object(x.jsx)("tr",Object(H.a)(Object(H.a)({},e.getRowProps()),{},{children:e.cells.map((function(e){return Object(x.jsx)("td",Object(H.a)(Object(H.a)({className:"transcript_cell"},e.getCellProps()),{},{children:e.render("Cell")}))}))}))}))}))]})),Object(x.jsx)("br",{})]})}var J=function(e){var t=e.CSEData,r=[],s={outterMostDiv:{float:"left",padding:"15px"}};if(0!=t["CSE-HSS"].completed.courses.length||0!=t["CSE-HSS"].in_progress.courses.length){var n,c,a={type:"CSE_HSS",inProgress:[],credit_hours:0,completed:[]};if(0!=t["CSE-HSS"].completed.courses.length)(n=a.completed).push.apply(n,Object(w.a)(t["CSE-HSS"].completed.courses)),a.credit_hours+=t["CSE-HSS"].completed.credit_hours;if(0!=t["CSE-HSS"].in_progress.courses.length)(c=a.completed).push.apply(c,Object(w.a)(t["CSE-HSS"].in_progress.courses)),a.credit_hours+=t["CSE-HSS"].in_progress.credit_hours;r.push(a)}if(0!=t["CSE-OPEN"].completed.courses.length||0!=t["CSE-OPEN"].in_progress.courses.length){var o,i,l={type:"CSE-OPEN",inProgress:[],credit_hours:0,completed:[]};if(0!=t["CSE-OPEN"].completed.courses.length)(o=l.completed).push.apply(o,Object(w.a)(t["CSE-OPEN"].completed.courses)),l.credit_hours+=t["CSE-OPEN"].completed.credit_hours;if(0!=t["CSE-OPEN"].in_progress.courses.length)(i=l.completed).push.apply(i,Object(w.a)(t["CSE-OPEN"].in_progress.courses)),l.credit_hours+=t["CSE-OPEN"].in_progress.credit_hours;r.push(l)}if(0!=t["CSE-ITS"].completed.courses.length||0!=t["CSE-ITS"].in_progress.courses.length){var u,d,j={type:"CSE-ITS",inProgress:[],credit_hours:0,completed:[]};if(0!=t["CSE-ITS"].completed.courses.length)(u=j.completed).push.apply(u,Object(w.a)(t["CSE-ITS"].completed.courses)),j.credit_hours+=t["CSE-ITS"].completed.credit_hours;if(0!=t["CSE-ITS"].in_progress.courses.length)(d=j.completed).push.apply(d,Object(w.a)(t["CSE-ITS"].in_progress.courses)),j.credit_hours+=t["CSE-ITS"].in_progress.credit_hours;r.push(j)}return Object(x.jsx)(x.Fragment,{children:r.map((function(e,t){return Object(x.jsx)("div",{style:s.outterMostDiv,children:Object(x.jsxs)("p",{children:[e.type," \xa0 ",e.inProgress.length+e.completed.length,"\xa0 (",e.credit_hours,"ch) ",e.inProgress.map((function(e){return Object(x.jsxs)("p",{children:[e," inprogress "]})})),e.completed.map((function(e){return Object(x.jsxs)("p",{children:[" ",e," completed"]})}))]})})}))})},K=function(e){var t=e.data,r={CourseCode:{display:"inline-block",font:"sans-serif",fontSize:"18px",wordBreak:"keep-all"},div_style:{boxShadow:"1px 3px 1px #9E9E9E"},CourseHeaders:{font:"sans-serif",fontSize:"20px",paddingBottom:"15px",paddingTop:"15px"},Parent_Div:{}},s=t.progress;return Object(x.jsxs)("div",{style:r.Parent_Div,children:[Object(x.jsx)("div",{children:Object(x.jsxs)("p",{children:["Audit: ",t.target_student.student_number,", \xa0",t.target_student.cohort,",\xa0"," ",t.target_student.rank,", \xa0years in:"," ",t.target_student.years_in]})}),Object(x.jsxs)("div",{children:[Object(x.jsxs)("p",{children:["Based on: ",t.base_program]})," "]}),Object(x.jsxs)("div",{children:["\xa0STATUS:\xa0",t.target_student.status]}),Object(x.jsxs)("div",{style:r.div_style,children:[Object(x.jsxs)("p",{children:["Progress through CORE\xa0("," ",s.CORE.completed.courses.length+s.CORE.remaining.courses.length+s.CORE.in_progress.courses.length,"\xa0courses,"," ",s.CORE.completed.credit_hours+s.CORE.remaining.credit_hours+s.CORE.in_progress.credit_hours,"\xa0CH)\xa0\xa0\xa0",s.CORE.remaining.courses.length,"\xa0courses (",s.CORE.remaining.credit_hours,"CH)\xa0 REMAINING"]})," "]}),Object(x.jsxs)("div",{style:r.CourseHeaders,children:["Core Courses completed: \xa0\xa0\xa0",s.CORE.completed.courses.length,"\xa0 courses \xa0(",s.CORE.completed.credit_hours,"CH)\xa0"]}),Object(x.jsx)("lu",{children:s.CORE.completed.courses.map((function(e){return Object(x.jsxs)("li",{style:r.CourseCode,children:["\xa0",e]})}))}),Object(x.jsxs)("div",{style:r.CourseHeaders,children:["Core Courses in progress: \xa0\xa0\xa0",s.CORE.in_progress.courses.length,"\xa0 courses \xa0(",s.CORE.in_progress.credit_hours,"CH)\xa0"]}),Object(x.jsx)("lu",{children:s.CORE.in_progress.courses.map((function(e){return Object(x.jsxs)("li",{style:r.CourseCode,children:["\xa0",e]})}))}),Object(x.jsxs)("div",{style:r.CourseHeaders,children:["Core Courses remaining: \xa0\xa0\xa0",s.CORE.remaining.courses.length,"\xa0 courses \xa0(",s.CORE.remaining.credit_hours,"CH)\xa0"]}),Object(x.jsx)("lu",{children:s.CORE.remaining.courses.map((function(e){return Object(x.jsxs)("li",{style:r.CourseCode,children:["\xa0",e]})}))}),Object(x.jsxs)("div",{style:r.div_style,children:[Object(x.jsxs)("p",{children:["Progress through TE\xa0("," ",s.TE.completed.courses.length+s.TE.remaining.num_courses+s.TE.in_progress.courses.length,"\xa0courses,"," ",s.TE.completed.credit_hours+s.TE.remaining.credit_hours+s.TE.in_progress.credit_hours,"\xa0CH)\xa0\xa0\xa0",s.TE.remaining.num_courses,"\xa0courses (",s.TE.remaining.credit_hours,"CH)\xa0 REMAINING"]})," "]}),Object(x.jsxs)("div",{style:r.CourseHeaders,children:["TE Courses completed: \xa0\xa0\xa0",s.TE.completed.courses.length,"\xa0 courses \xa0(",s.TE.completed.credit_hours,"CH)\xa0"]}),Object(x.jsx)("lu",{children:s.TE.completed.courses.map((function(e){return Object(x.jsxs)("li",{style:r.CourseCode,children:["\xa0",e]})}))}),Object(x.jsxs)("div",{style:r.CourseHeaders,children:["TE Courses in progress: \xa0\xa0\xa0",s.TE.in_progress.courses.length,"\xa0 courses \xa0(",s.TE.in_progress.credit_hours,"CH)\xa0"]}),Object(x.jsx)("lu",{children:s.TE.in_progress.courses.map((function(e){return Object(x.jsxs)("li",{style:r.CourseCode,children:["\xa0",e]})}))})," ",Object(x.jsxs)("div",{style:r.div_style,children:[Object(x.jsxs)("p",{children:["Progress through NS\xa0("," ",s.NS.completed.courses.length+s.NS.remaining.num_courses+s.NS.in_progress.courses.length,"\xa0courses,"," ",s.NS.completed.credit_hours+s.NS.remaining.credit_hours+s.NS.in_progress.credit_hours,"\xa0CH)\xa0\xa0\xa0",s.NS.remaining.num_courses,"\xa0courses (",s.NS.remaining.credit_hours,"CH)\xa0 REMAINING"]})," "]}),Object(x.jsxs)("div",{style:r.CourseHeaders,children:["NS Courses completed: \xa0\xa0\xa0",s.NS.completed.courses.length,"\xa0 courses \xa0(",s.NS.completed.credit_hours,"CH)\xa0"]}),Object(x.jsx)("div",{children:s.NS.completed.courses.map((function(e){return Object(x.jsxs)("li",{style:r.CourseCode,children:["\xa0",e]})}))}),Object(x.jsxs)("div",{style:r.CourseHeaders,children:["NS Courses in progress: \xa0\xa0\xa0",s.NS.in_progress.courses.length,"\xa0 courses \xa0(",s.NS.in_progress.credit_hours,"CH)\xa0"]}),Object(x.jsx)("div",{children:s.NS.in_progress.courses.map((function(e){return Object(x.jsxs)("li",{style:r.CourseCode,children:["\xa0",e]})}))})," ",Object(x.jsxs)("div",{style:r.div_style,children:[Object(x.jsxs)("p",{children:["Progress through CSE\xa0("," ",s["CSE-ITS"].completed.courses.length," ","\xa0ITS,\xa0",s["CSE-HSS"].completed.courses.length," ","\xa0HSS,\xa0",s["CSE-OPEN"].completed.courses.length," \xa0OPEN \xa0;"," ",s["CSE-HSS"].completed.credit_hours+s["CSE-OPEN"].completed.credit_hours+s["CSE-ITS"].completed.credit_hours,"\xa0CH)\xa0\xa0\xa0",s["CSE-ITS"].remaining.num_courses,"\xa0courses (",s["CSE-ITS"].remaining.credit_hours,"CH)\xa0 REMAINING"]})," "]}),Object(x.jsx)(J,{CSEData:s})]})};r(108),r(119),r(138);var Y=function(){var e=n.a.useState([]),t=Object(u.a)(e,2),r=t[0],s=t[1],c=n.a.useState([]),a=Object(u.a)(c,2),o=a[0],d=a[1],j=n.a.useState(!1),h=Object(u.a)(j,2),p=h[0],b=h[1],O=n.a.useState([]),m=Object(u.a)(O,2),g=m[0],f=m[1],E=n.a.useState(!1),N=Object(u.a)(E,2),I=N[0],H=N[1],w=n.a.useState(!1),P=Object(u.a)(w,2),F=(P[0],P[1],n.a.useState(!0)),R=Object(u.a)(F,2),k=(R[0],R[1],n.a.useState({name:"",program:"",campus:"",rank:"",status:""})),A=Object(u.a)(k,2),D=A[0],L=A[1],G=n.a.useState([]),J=Object(u.a)(G,2),Y=J[0],W=J[1],$=n.a.useState(!1),q=Object(u.a)($,2),Q=q[0],X=q[1],Z=function(){return X(!1)};n.a.useEffect((function(){Object(l.a)(i.a.mark((function e(){return i.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,_(s);case 2:case"end":return e.stop()}}),e)})))()}),[]);var ee=n.a.useState({}),te=Object(u.a)(ee,2),re=te[0],se=te[1];function ne(e){var t=e.audit;return t||I?t?Object(x.jsxs)(U.a,{show:Q,onHide:Z,"aria-labelledby":"example-modal-sizes-title-lg",size:"xl",children:[Object(x.jsxs)(U.a.Header,{closeButton:!0,children:[Object(x.jsx)(C.a,{size:"lg",variant:"outline-secondary",onClick:function(){return b(!1)},children:"Transcript"}),Object(x.jsx)(C.a,{size:"lg",variant:"outline-secondary",onClick:function(){return b(!0)},children:"Audit"})]}),Object(x.jsx)(U.a.Body,{children:Object(x.jsxs)("div",{style:{boxShadow:"1px 3px 1px #9E9E9E",display:"inline-block"},children:[Object(x.jsx)(C.a,{size:"lg",variant:"outline-secondary",children:"Generate Text Audit"}),Object(x.jsx)(K,{data:re})]})}),Object(x.jsx)(U.a.Footer,{children:Object(x.jsx)(C.a,{variant:"secondary",onClick:Z,children:"Close"})})]}):Object(x.jsx)(U.a,{show:Q,onHide:Z,"aria-labelledby":"example-modal-sizes-title-lg",size:"xl",children:Object(x.jsx)("div",{className:"spin"})}):Object(x.jsx)(x.Fragment,{children:Object(x.jsxs)(U.a,{show:Q,onHide:Z,"aria-labelledby":"example-modal-sizes-title-lg",size:"xl",children:[Object(x.jsxs)(U.a.Header,{closeButton:!0,children:[Object(x.jsx)(C.a,{size:"lg",variant:"outline-secondary",onClick:function(){return b(!1)},children:"Transcript"}),Object(x.jsx)(C.a,{size:"lg",variant:"outline-secondary",onClick:function(){return b(!0)},children:"Audit"})]}),Object(x.jsx)(U.a.Body,{children:Object(x.jsxs)("div",{className:"row_modal",children:[Object(x.jsx)("div",{className:"column_modal",children:Object(x.jsx)(V,{columns:M,data:o})}),Object(x.jsxs)("div",{className:"column_modal",children:[Object(x.jsx)("h1",{style:{fontFamily:"sans-serif"},children:D.name}),Object(x.jsx)("br",{}),Object(x.jsx)("h4",{style:{fontFamily:"sans-serif"},children:g}),Object(x.jsx)("h4",{style:{fontFamily:"sans-serif"},children:D.program}),Object(x.jsx)("h4",{style:{fontFamily:"sans-serif"},children:D.campus}),Object(x.jsx)("h4",{style:{fontFamily:"sans-serif"},children:D.rank}),Object(x.jsx)("h4",{style:{fontFamily:"sans-serif"},children:D.status})]})]})}),Object(x.jsx)(U.a.Footer,{children:Object(x.jsx)(C.a,{variant:"secondary",onClick:Z,children:"Close"})})]})})}return n.a.useEffect((function(){Object(l.a)(i.a.mark((function e(){return i.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,T(g,se);case 2:return e.next=4,y(g,d,H);case 4:case"end":return e.stop()}}),e)})))()}),[g]),Object(x.jsx)(x.Fragment,{children:Object(x.jsxs)("div",{className:"master-container",children:[Object(x.jsxs)("div",{className:"div-table",children:[Object(x.jsx)(ne,{audit:p}),Object(x.jsx)(z,{columns:B,data:r,modalClose:Z,modalOpen:function(){return X(!0)},modalState:Q,selectKey:f,selectRow:L,updateChecked:W,setTranLoad:H})]}),Object(x.jsx)("div",{className:"div-textAudit",children:Object(x.jsx)(v,{checked:Y})}),Object(x.jsx)("div",{className:"div-counts",children:Object(x.jsx)(S,{})})]})})},W=function(e){e&&e instanceof Function&&r.e(3).then(r.bind(null,151)).then((function(t){var r=t.getCLS,s=t.getFID,n=t.getFCP,c=t.getLCP,a=t.getTTFB;r(e),s(e),n(e),c(e),a(e)}))};a.a.render(Object(x.jsx)(Y,{}),document.getElementById("root")),W()},65:function(e,t,r){},83:function(e,t,r){}},[[139,1,2]]]);
//# sourceMappingURL=main.5c167704.chunk.js.map