(this["webpackJsonp4103-table"]=this["webpackJsonp4103-table"]||[]).push([[0],{100:function(e,t,r){},101:function(e,t,r){"use strict";r.r(t);var c=r(0),n=r.n(c),s=r(18),a=r.n(s),l=(r(75),r(13)),i=r.n(l),o=r(33),d=r(2),u=r(5),j=r(23),b=r(20),O=(r(52),r(108)),h=r(69),p=r(112),m=r(109),x=r(66),f=r(110),v=r(62),N=r.n(v),g=(r(96),r(1));function S(){var e=Object(c.useState)({title:"Cohort",input:"2021-01-01"}),t=Object(u.a)(e,2),r=t[0],n=t[1],s=Object(c.useState)({coop:0,total:0,FIR:0,SOP:0,JUN:0,SEN:0}),a=Object(u.a)(s,2),l=a[0],i=a[1];return Object(c.useEffect)((function(){var e="",t=0;"cohort"===r.title.toLowerCase()?e="http://127.0.0.1:8000/api/counts_start_date/"+r.input:(e="http://127.0.0.1:8000/api/counts_semester/"+r.input,t=1),[/\d{4}-\d{2}-\d{2}$/,/\d{4}\/FA|WI|SM$/][t].test(r.input)&&N.a.get(e).then((function(e){i({coop:e.data.countCoop,total:e.data.countTotal,FIR:e.data.FIR,SOP:e.data.SOP,JUN:e.data.JUN,SEN:e.data.SEN})}))}),[r]),Object(g.jsxs)("div",{className:"countsCard",children:[Object(g.jsxs)("div",{className:"headerDiv",children:[Object(g.jsx)("div",{className:"dropdownDiv",children:Object(g.jsxs)(O.a,{id:"dropdown-basic-button",title:r.title,variant:"danger",onSelect:function(e){return n({title:e,input:r.input})},children:[Object(g.jsx)(h.a.Item,{eventKey:"Cohort",children:"Cohort"}),Object(g.jsx)(h.a.Item,{eventKey:"Semester",children:"Semester"})]})}),Object(g.jsx)("div",{className:"formDiv",children:Object(g.jsx)(p.a,{children:Object(g.jsx)(m.a,{children:Object(g.jsx)(x.a,{children:Object(g.jsx)("input",{className:"inputValueForm",type:"text",placeholder:r.input,onChange:function(e){return n({title:r.title,input:e.target.value})}})})})})})]}),Object(g.jsx)("br",{}),Object(g.jsx)("div",{className:"tableDiv",children:Object(g.jsxs)(f.a,{hover:!0,size:"sm",children:[Object(g.jsx)("thead",{children:Object(g.jsxs)("tr",{children:[Object(g.jsx)("th",{}),Object(g.jsx)("th",{children:"Count"})]})}),Object(g.jsxs)("tbody",{className:"counts_tbody",children:[Object(g.jsxs)("tr",{children:[Object(g.jsx)("td",{children:"Total"}),Object(g.jsx)("td",{children:l.total})]}),Object(g.jsxs)("tr",{children:[Object(g.jsx)("td",{children:"Coop"}),Object(g.jsx)("td",{children:l.coop})]}),Object(g.jsxs)("tr",{children:[Object(g.jsx)("td",{children:"FIR"}),Object(g.jsx)("td",{children:l.FIR})]}),Object(g.jsxs)("tr",{children:[Object(g.jsx)("td",{children:"SOP"}),Object(g.jsx)("td",{children:l.SOP})]}),Object(g.jsxs)("tr",{children:[Object(g.jsx)("td",{children:"JUN"}),Object(g.jsx)("td",{children:l.JUN})]}),Object(g.jsxs)("tr",{children:[Object(g.jsx)("td",{children:"SEN"}),Object(g.jsx)("td",{children:l.SEN})]})]})]})})]})}var F=r(67);r(100);function C(e){return y.apply(this,arguments)}function y(){return(y=Object(o.a)(i.a.mark((function e(t){var r,c,n;return i.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return"http://127.0.0.1:8000/api/student_data",e.next=3,fetch("http://127.0.0.1:8000/api/student_data");case 3:return r=e.sent,e.next=6,r.json();case 6:return c=e.sent,e.next=9,c.map((function(e){return e.fields}));case 9:return n=e.sent,console.log(n),e.abrupt("return",t(n));case 12:case"end":return e.stop()}}),e)})))).apply(this,arguments)}function I(e,t){return T.apply(this,arguments)}function T(){return(T=Object(o.a)(i.a.mark((function e(t,r){var c,n,s;return i.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(0===t.length){e.next=11;break}return console.log(t),c="http://127.0.0.1:8000/get_transcript/"+t[0],e.next=5,fetch(c);case 5:return n=e.sent,e.next=8,n.json();case 8:return s=e.sent,console.log(s),e.abrupt("return",r(s));case 11:case"end":return e.stop()}}),e)})))).apply(this,arguments)}var w=r(64),H=r(111);function P(e){var t=e.column,r=t.filterValue,c=t.preFilteredRows,n=t.setFilter;c.length;return Object(g.jsx)("input",{value:r||"",onChange:function(e){n(e.target.value||void 0)},placeholder:"Search Records..."})}function _(e){var t=e.column,r=t.filterValue,c=t.setFilter,s=t.preFilteredRows,a=t.id,l=n.a.useMemo((function(){var e=new Set;return s.forEach((function(t){e.add(t.values[a])})),Object(j.a)(e.values())}),[a,s]);return Object(g.jsxs)("select",{value:r,onChange:function(e){c(e.target.value||void 0)},children:[Object(g.jsx)("option",{value:"",children:"All"}),l.map((function(e,t){return Object(g.jsx)("option",{value:e,children:e},t)}))]})}function E(e,t,r){return Object(F.a)(e,r,{keys:[function(e){return e.values[t]}]})}function R(e){var t=e.columns,r=e.data,c=(e.modalClose,e.modalOpen),s=(e.modalState,e.selectKey),a=e.selectName;var l=n.a.useMemo((function(){return{fuzzyText:E,text:function(e,t,r){return e.filter((function(e){var c=e.values[t];return void 0===c||String(c).toLowerCase().startsWith(String(r).toLowerCase())}))}}}),[]),i=n.a.useMemo((function(){return{Filter:P}}),[]),o=Object(b.useTable)({columns:t,data:r,defaultColumn:i,filterTypes:l},b.useFilters,b.useGlobalFilter,b.useSortBy),u=o.getTableProps,j=o.getTableBodyProps,O=o.headerGroups,h=o.rows,p=o.prepareRow,m=o.state,x=o.visibleColumns,f=h;return Object(g.jsxs)(g.Fragment,{children:[Object(g.jsxs)("table",Object(d.a)(Object(d.a)({className:"styled-table"},u()),{},{children:[Object(g.jsxs)("thead",{children:[O.map((function(e){return Object(g.jsx)("tr",Object(d.a)(Object(d.a)({},e.getHeaderGroupProps()),{},{children:e.headers.map((function(e){return Object(g.jsxs)("th",Object(d.a)(Object(d.a)({},e.getHeaderProps(e.getSortByToggleProps())),{},{children:[e.render("Header"),Object(g.jsxs)("div",{children:[e.canFilter?e.render("Filter"):null,Object(g.jsxs)("span",{children:[e.isSorted?e.isSortedDesc?"\ud83d\udd3d":"\ud83d\udd3c":""," "]})]})]}))}))}))})),Object(g.jsx)("tr",{children:Object(g.jsx)("th",{colSpan:x.length})})]}),Object(g.jsx)("tbody",Object(d.a)(Object(d.a)({},j()),{},{children:f.map((function(e,t){return p(e),Object(g.jsx)("tr",Object(d.a)(Object(d.a)({onClick:function(){return function(e){var t=e.cells.map((function(e){if("student_number"===e.column.id)return e.value})),r=e.cells.map((function(e){if("name"===e.column.id)return e.value}));c(),a(r),s(t),console.log(t)}(e)}},e.getRowProps()),{},{children:e.cells.map((function(e){return Object(g.jsx)("td",Object(d.a)(Object(d.a)({className:"table-td-cell"},e.getCellProps()),{},{children:e.render("Cell")}))}))}))}))}))]})),Object(g.jsx)("br",{}),Object(g.jsx)("div",{children:Object(g.jsx)("pre",{children:Object(g.jsx)("code",{children:JSON.stringify(m.filters,null,2)})})})]})}function k(e){var t=e.columns,r=e.data,c=(e.modalClose,e.modalOpen,e.modalState,e.selectKey,e.selectName,n.a.useMemo((function(){return{fuzzyText:E,text:function(e,t,r){return e.filter((function(e){var c=e.values[t];return void 0===c||String(c).toLowerCase().startsWith(String(r).toLowerCase())}))}}}),[])),s=Object(b.useTable)({columns:t,data:r,filterTypes:c},b.useFilters,b.useGlobalFilter,b.useSortBy),a=s.getTableProps,l=s.getTableBodyProps,i=s.headerGroups,o=s.rows,u=s.prepareRow,j=s.state,O=s.visibleColumns,h=o;return Object(g.jsxs)(g.Fragment,{children:[Object(g.jsxs)(f.a,Object(d.a)(Object(d.a)({className:"styled-transcript"},a()),{},{children:[Object(g.jsxs)("thead",{className:"styled-transcript-thead",children:[i.map((function(e){return Object(g.jsx)("tr",Object(d.a)(Object(d.a)({},e.getHeaderGroupProps()),{},{children:e.headers.map((function(e){return Object(g.jsxs)("th",Object(d.a)(Object(d.a)({className:"transcript_head"},e.getHeaderProps(e.getSortByToggleProps())),{},{children:[e.render("Header"),Object(g.jsxs)("div",{children:[e.canFilter?e.render("Filter"):null,Object(g.jsxs)("span",{children:[e.isSorted?e.isSortedDesc?"\ud83d\udd3d":"\ud83d\udd3c":""," "]})]})]}))}))}))})),Object(g.jsx)("tr",{children:Object(g.jsx)("th",{colSpan:O.length})})]}),Object(g.jsx)("tbody",Object(d.a)(Object(d.a)({className:"styled-transcript-tbody"},l()),{},{children:h.map((function(e,t){return u(e),Object(g.jsx)("tr",Object(d.a)(Object(d.a)({},e.getRowProps()),{},{children:e.cells.map((function(e){return Object(g.jsx)("td",Object(d.a)(Object(d.a)({className:"transcript_cell"},e.getCellProps()),{},{children:e.render("Cell")}))}))}))}))}))]})),Object(g.jsx)("br",{}),Object(g.jsx)("div",{children:Object(g.jsx)("pre",{children:Object(g.jsx)("code",{children:JSON.stringify(j.filters,null,2)})})})]})}function B(e,t,r,c){var n=e.values[r];n=n.split("*"),console.log(n);var s=t.values[r];s=s.split("*"),console.log(s);var a=Number.parseFloat(n[1]),l=Number.parseFloat(s[1]);return Number.isNaN(a)&&(a=c?Number.NEGATIVE_INFINITY:Number.POSITIVE_INFINITY),Number.isNaN(l)&&(l=c?Number.NEGATIVE_INFINITY:Number.POSITIVE_INFINITY),a>l?1:a<l?-1:0}E.autoRemove=function(e){return!e};var G=function(){var e=n.a.useState([]),t=Object(u.a)(e,2),r=t[0],c=t[1],s=n.a.useState([]),a=Object(u.a)(s,2),l=a[0],d=a[1],j=n.a.useState(!1),b=Object(u.a)(j,2),O=b[0],h=b[1],p=n.a.useState([]),m=Object(u.a)(p,2),x=m[0],f=m[1],v=n.a.useState(""),N=Object(u.a)(v,2),F=N[0],y=N[1],T=function(){return h(!1)};n.a.useEffect((function(){Object(o.a)(i.a.mark((function e(){return i.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,C(c);case 2:case"end":return e.stop()}}),e)})))()}),[]),n.a.useEffect((function(){Object(o.a)(i.a.mark((function e(){return i.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,I(x,d);case 2:case"end":return e.stop()}}),e)})))()}),[x]);var P=n.a.useMemo((function(){return[{Header:" ",columns:[{Header:"Student ID",accessor:"student_number"},{Header:"Name",accessor:"name"},{Header:"Program",accessor:"program"},{Header:"Campus",accessor:"campus",Filter:_,filter:"includes"},{Header:"Rank",accessor:"rank",Filter:_}]}]}),[]),E=n.a.useMemo((function(){return[{Header:" ",columns:[{Header:"Course Code",accessor:"Course_Code",sortType:B,disableFilters:!0},{Header:"Course Name",accessor:"Course_Name",disableFilters:!0},{Header:"Course Type",accessor:"Course_Type",disableFilters:!0},{Header:"Semester",accessor:"Semester",disableFilters:!0},{Header:"Section",accessor:"Section",filter:"includes",disableFilters:!0},{Header:"Credit Hours",accessor:"Credit_Hours",disableFilters:!0},{Header:"Grade",accessor:"Grade",disableFilters:!0}]}]}),[]);return Object(g.jsx)(g.Fragment,{children:Object(g.jsxs)("div",{className:"master-container",children:[Object(g.jsxs)("div",{className:"div-table",children:[Object(g.jsxs)(H.a,{show:O,onHide:T,"aria-labelledby":"example-modal-sizes-title-lg",size:"xl",children:[Object(g.jsx)(H.a.Header,{closeButton:!0,children:Object(g.jsx)(H.a.Title,{children:"Transcript"})}),Object(g.jsx)(H.a.Body,{children:Object(g.jsxs)("div",{className:"row_modal",children:[Object(g.jsx)("div",{className:"column_modal",children:Object(g.jsx)(k,{columns:E,data:l})}),Object(g.jsxs)("div",{className:"column_modal",children:[Object(g.jsx)("h1",{children:F}),Object(g.jsx)("br",{}),Object(g.jsx)("h2",{children:x})]})]})}),Object(g.jsx)(H.a.Footer,{children:Object(g.jsx)(w.a,{variant:"secondary",onClick:T,children:"Close"})})]}),Object(g.jsx)(R,{columns:P,data:r,modalClose:T,modalOpen:function(){return h(!0)},modalState:O,selectKey:f,selectName:y})]}),Object(g.jsx)("div",{className:"div-counts",children:Object(g.jsx)(S,{})})]})})},J=function(e){e&&e instanceof Function&&r.e(3).then(r.bind(null,113)).then((function(t){var r=t.getCLS,c=t.getFID,n=t.getFCP,s=t.getLCP,a=t.getTTFB;r(e),c(e),n(e),s(e),a(e)}))};a.a.render(Object(g.jsx)(G,{}),document.getElementById("root")),J()},75:function(e,t,r){},96:function(e,t,r){}},[[101,1,2]]]);
//# sourceMappingURL=main.21177020.chunk.js.map