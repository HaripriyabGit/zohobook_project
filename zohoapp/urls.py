from django.urls import path,include,re_path
from.import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
#from .views import EmailAttachementView

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('base', views.base, name='base'),
    path('logout', views.logout, name='logout'),
    path('forgotpassword' , views.forgotpassword,name='forgotpassword'),  
    path('setnewpassword' , views.setnewpassword,name='setnewpassword'),   

    path('view_profile', views.view_profile, name='view_profile'),
    path('edit_profile/<pk>', views.edit_profile, name='edit_profile'),
    path('itemview',views.itemview,name='itemview'),
    path('additem',views.additem,name='additem'),
    path('add',views.add,name='add'),
    path('add_account',views.add_account,name='add_account'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('edititem/<int:id>',views.edititem,name='edititem'),
    path('edit_db/<int:id>',views.edit_db,name='edit_db'),
    path('Action/<int:id>',views.Action,name='Action'),
    path('cleer/<int:id>',views.cleer,name='cleer'),
    path('add_unit',views.add_unit,name='add_unit'),
    path('sales',views.add_sales,name='add_sales'),
    path('vendor/',views.vendor,name='vendor'),
    path('add_vendor/',views.add_vendor,name='add_vendor'),
    path('sample/',views.sample,name="sample"),
    path('view_vendor_list/',views.view_vendor_list,name='view_vendor_list'),
    path('view_vendor_details/<int:pk>',views.view_vendor_details,name='view_vendor_details'),
    path('add_comment/<int:pk>',views.add_comment,name='add_comment'),
    path('sendmail/<int:pk>',views.sendmail,name='sendmail'),
    path('edit_vendor/<int:pk>',views.edit_vendor,name='edit_vendor'),
    path('edit_vendor_details/<int:pk>',views.edit_vendor_details,name='edit_vendor_details'),
    path('upload_document/<int:pk>',views.upload_document,name='upload_document'),
    path('download_doc/<int:pk>',views.download_doc,name='download_doc'),
    path('cancel_vendor/',views.cancel_vendor,name='cancel_vendor'),
    path('delete_vendor/<int:pk>',views.delete_vendor,name='delete_vendor'),
    path('add_customer/',views.add_customer,name='add_customer'),
    path('retainer_invoices/',views.retainer_invoice,name='retainer_invoice'),
    path('add_invoice/',views.add_invoice,name='add_invoice'),
    path('create_invoice_draft/',views.create_invoice_draft,name='create_invoice_draft'),
    path('create_invoice_send/',views.create_invoice_send,name='create_invoice_send'),
    path('view_invoice/<int:pk>',views.invoice_view,name='invoice_view'),
    path('retainer_template/<int:pk>',views.retainer_template,name='retainer_template'),
    path('retainer_invoice_edit/<int:pk>',views.retainer_edit_page,name='retainer_edit_page'), 
    path('retainer_invoice_update/<int:pk>',views.retainer_update,name='retainer_update'),
   # path('send_mail/<int:pk>',views.mail_send,name='mail_send'),
    path('retaineritem_delete/<int:pk>',views.retaineritem_delete,name='retaineritem_delete'),
    path('retainer_delete/<int:pk>',views.retainer_delete,name='retainer_delete'),
    path('allestimates',views.allestimates,name='allestimates'),
    path('newestimate/',views.newestimate,name='newestimate'),
    path('createestimate/',views.createestimate,name='createestimate'),
    path('itemdata_est/',views.itemdata_est,name='itemdata_est'),
    path('create_and_send_estimate/',views.create_and_send_estimate,name='create_and_send_estimate'),
    path('estimateslip/<int:est_id>',views.estimateslip,name='estimateslip'),
    path('editestimate/<int:est_id>',views.editestimate,name='editestimate'),
    path('updateestimate/<int:pk>',views.updateestimate,name='updateestimate'),
    path('converttoinvoice/<int:est_id>',views.converttoinvoice,name='converttoinvoice'),
    #path('emailattachment', EmailAttachementView.as_view(), name='emailattachment'),
    path('add_customer_for_estimate/',views.add_customer_for_estimate,name='add_customer_for_estimate'),
    path('entr_custmr_for_estimate/',views.entr_custmr_for_estimate,name='entr_custmr_for_estimate'),
    path('payment_term_for_estimate/',views.payment_term_for_estimate,name='payment_term_for_estimate'),
    path('invoiceview',views.invoiceview,name='invoiceview'),
    path('addinvoice',views.addinvoice,name='addinvoice'),
    path('itemdata',views.itemdata,name='itemdata'),
    path('add_prod',views.add_prod,name='add_prod'),
    path('detailedview/<int:id>',views.detailedview,name='detailedview'),
    path('edited_prod/<int:id>',views.edited_prod,name='edited_prod'),
    path('dele/<int:pk>',views.dele,name='dele'),
    # path('edited/<int:id>',views.edited,name='edited'),
    path('payment_term',views.payment_term,name='payment_term'),
    path('add_cx',views.add_cx,name="add_cx"),
    path('deleteestimate/<int:est_id>',views.deleteestimate,name='deleteestimate'),
    path('additem_est',views.additem_est,name='additem_est'),
    path('additem_page_est',views.additem_page_est,name='additem_page_est'),
    path('add_unit_est',views.add_unit_est,name='add_unit_est'),
    path('add_sales_est',views.add_sales_est,name='add_sales_est'),
    path('add_account_est',views.add_account_est,name='add_account_est'),
    path('customerdata', views.customerdata, name='customerdata'),
    path('add_customer_for_invoice',views.add_customer_for_invoice,name='add_customer_for_invoice'),
    path('payment_term_for_invoice',views.payment_term_for_invoice,name='payment_term_for_invoice'),
    path('addprice',views.addprice,name='addprice'),
    path('addpl',views.addpl,name='addpl'),
    path('viewpricelist',views.viewpricelist,name='viewpricelist'),
    path('viewlist/<int:id>',views.viewlist,name='viewlist'),
    path('editlist/<int:id>',views.editlist,name='editlist'),
    path('editpage/<int:id>',views.editpage,name='editpage'),
    path('delete_item/<int:id>',views.delete_item,name='delete_item'),
    path('active_status/<int:id>',views.active_status,name='active_status'),
    path('createpl',views.createpl,name='createpl'),
    path('banking_home',views.banking_home,name='banking_home'),
    path('create_banking',views.create_banking,name='create_banking'),
    path('save_banking',views.save_banking,name='save_banking'),
    path('view_bank/<int:id>',views.view_bank,name='view_bank'),
    path('banking_edit/<int:id>',views.banking_edit,name='banking_edit'),
    path('save_edit_bnk/<int:id>',views.save_edit_bnk,name='save_edit_bnk'),
    path('save_banking_edit/<int:id>',views.save_banking_edit,name='save_banking_edit'),
    path('save_bank',views.save_bank,name='save_bank'),
    path('banking_delete/<int:id>',views.banking_delete,name='banking_delete'),
    path('entr_custmr',views.entr_custmr,name='entr_custmr'),
    path('get_customer_names', views.get_customer_names, name='get_customer_names'),
    path('expense/delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),
    path('get_profile_details/<int:profile_id>/', views.get_profile_details, name='get_profile_details'),
    path('recurringhome',views.recurringhome,name='recurringhome'),
    path('add_expense',views.add_expense,name='add_expense'),
    path('recurringbase',views.recurringbase,name='recurringbase'),
    path('show_recurring/<int:expense_id>/', views.show_recurring, name='show_recurring'),
    path('expense_details', views.expense_details, name='expense_details'),
    path('edit_expense/<int:expense_id>/', views.edit_expense, name='edit_expense'),
    path('newexp',views.newexp,name='newexp'),
    path('save-data/', views.save_data, name='save_data'),
    path('get-account-names/', views.get_account_names, name='get_account_names'),
    path('profileshow',views.profileshow,name='profileshow'),
    path('add_customer',views.add_customer,name='add_customer'),
    
    path('view_sales_order',views.view_sales_order,name='view_sales_order'),
    path('create_sales_order',views.create_sales_order,name='create_sales_order'),
    path('add_customer_for_sorder',views.add_customer_for_sorder,name='add_customer_for_sorder'),
    path('payment_term_for_sorder',views.payment_term_for_sorder,name='payment_term_for_sorder'),

    path('add_sales_order',views.add_sales_order,name='add_sales_order'),
    path('sales_order_det/<int:id>',views.sales_order_det,name='sales_order_det'),
    path('edit_sales_order/<int:id>',views.edit_sales_order,name='edit_sales_order'),
    path('delet_sales/<int:id>',views.delet_sales,name='delet_sales'),
    
    path('create_delivery_chellan',views.create_delivery_chellan,name='create_delivery_chellan'),
    path('delivery_chellan_home',views.delivery_chellan_home,name='delivery_chellan_home'),
    path('add_customer_for_challan',views.add_customer_for_challan,name='add_customer_for_challan'),
    path('entr_custmr_for_challan',views.entr_custmr_for_challan,name='entr_custmr_for_challan'),
    path('additem_page_challan',views.additem_page_challan,name='additem_page_challan'),
    path('additem_challan',views.additem_challan,name='additem_challan'), 
    path('delivery_challan_view/<int:id>',views.delivery_challan_view,name='delivery_challan_view'),
    path('delivery_challan_edit/<int:id>',views.delivery_challan_edit,name='delivery_challan_edit'),
    path('update_challan/<int:id>',views.update_challan,name='update_challan'),
    path('create_and_send_challan',views.create_and_send_challan,name='create_and_send_challan'),
    path('create_challan_draft',views.create_challan_draft,name='create_challan_draft'),
    path('get_cust_mail',views.get_cust_mail,name='get_cust_mail'),
    path('additem_edit_challan',views.additem_edit_challan,name='additem_edit_challan'),
    path('additem_challan_edit',views.additem_challan_edit,name='additem_challan_edit'),
    path('add_customer_edit_challan',views.add_customer_edit_challan,name='add_customer_edit_challan'),
    path('sv_cust_edit_challan',views.sv_cust_edit_challan,name='sv_cust_edit_challan'),
    path('add_account_challan_edit',views.add_account_challan_edit,name='add_account_challan_edit'),
    path('add_unit_edit_challan',views.add_unit_edit_challan,name='add_unit_edit_challan'),
    path('add_sales_edit_challan',views.add_sales_edit_challan,name='add_sales_edit_challan'),
    path('payment_term_challan_edit',views.payment_term_challan_edit,name='payment_term_challan_edit'),
    path('payment_term_challan',views.payment_term_challan,name='payment_term_challan'),

    path('add_account_challan',views.add_account_challan,name='add_account_challan'),
    path('add_unit_challan',views.add_unit_challan,name='add_unit_challan'),
    path('add_sales_challan',views.add_sales_challan,name='add_sales_challan'),
    path('render_challan_pdf/<int:id>',views.render_challan_pdf,name='render_challan_pdf'),
    path('deletechallan/<int:id>',views.deletechallan,name='deletechallan'),
    
    path('filter_chellan',views.filter_chellan,name='filter_chellan'),
    path('filter_chellan_type',views.filter_chellan_type,name='filter_chellan_type'),
    path('itemdata_challan',views.itemdata_challan,name='itemdata_challan'),
    path('payment_term_for_sales',views.payment_term_for_sales,name="payment_term_for_sales"),
    
    path('report_page/',views.report_page,name='report_page'),
    path('report_recurring_invoice/',views.report_recurring_invoice,name='report_recurring_invoice'),
    
    path('create_recur',views.create_recur,name='create_recur'),
    path('new_recur',views.new_recur,name='new_recur'),
    path('view_recurpage',views.view_recurpage,name='view_recurpage'),
    path('viewrecur/<int:id>',views.viewrecur,name='viewrecur'),
    path('edit_recur/<int:id>',views.edit_recur,name='edit_recur'),
    path('editrecurpage<int:id>',views.editrecurpage,name='editrecurpage'),
    path('del_recur/<int:del_id>',views.del_recur,name='del_recur'),
    path('itemdata_recur',views.itemdata_recur,name='itemdata_recur'),
    path('payment_recur',views.payment_recur,name='payment_recur'),
    #path('customer_details',views.customer_details,name='customer_details'),
    
    path('recurring_bill',views.recurring_bill,name='recurring_bill'),
    path('recur_custasc',views.recur_custasc,name='recur_custasc'),
    path('recur_custdesc',views.recur_custdesc,name='recur_custdesc'),
    path('recur_vendorasc',views.recur_vendorasc,name='recur_vendorasc'),
    path('recur_vendordesc',views.recur_vendordesc,name='recur_vendordesc'),
    path('recur_profileasc',views.recur_profileasc,name='recur_profileasc'),
    path('recur_profiledesc',views.recur_profiledesc,name='recur_profiledesc'),
    path('add_recurring_bills',views.add_recurring_bills,name='add_recurring_bills'),
    path('create_recurring_bills',views.create_recurring_bills,name='create_recurring_bills'),
    path('edit_recurring_bills/<id>',views.edit_recurring_bills,name='edit_recurring_bills'),
    path('change_recurring_bills/<id>',views.change_recurring_bills,name='change_recurring_bills'),
    path('delete_recurring_bills/<id>',views.delete_recurring_bills,name='delete_recurring_bills'),
    path('view_recurring_bills/<id>',views.view_recurring_bills,name='view_recurring_bills'),
    path('view_custasc/<id>',views.view_custasc,name='view_custasc'),
    path('view_custdesc/<id>',views.view_custdesc,name='view_custdesc'),
    path('view_vendorasc/<id>',views.view_vendorasc,name='view_vendorasc'),
    path('view_vendordesc/<id>',views.view_vendordesc,name='view_vendordesc'),
    path('view_profileasc/<id>',views.view_profileasc,name='view_profileasc'),
    path('view_profiledesc/<id>',views.view_profiledesc,name='view_profiledesc'),
    path('get_vendordet',views.get_vendordet,name='get_vendordet'),
    path('get_customerdet',views.get_customerdet,name='get_customerdet'),
    path('recurbills_vendor',views.recurbills_vendor,name='recurbills_vendor'),
    path('vendor_dropdown',views.vendor_dropdown,name = 'vendor_dropdown'),
    path('recurbills_pay',views.recurbills_pay,name='recurbills_pay'),
    path('pay_dropdown',views.pay_dropdown,name = 'pay_dropdown'),
    path('recurbills_unit',views.recurbills_unit,name='recurbills_unit'),
    path('unit_dropdown',views.unit_dropdown,name = 'unit_dropdown'),
    path('recurbills_item',views.recurbills_item,name='recurbills_item'),
    path('item_dropdown',views.item_dropdown ,name = 'item_dropdown'),
    path('recurbills_account',views.recurbills_account,name='recurbills_account'),
    path('account_dropdown',views.account_dropdown ,name = 'account_dropdown'),
    path('get_rate',views.get_rate ,name = 'get_rate'),
    path('get_cust_state',views.get_cust_state,name = "get_cust_state"),
    path('export_pdf/<id>',views.export_pdf,name = "export_pdf"),
    path('recurbill_comment',views.recurbill_comment,name = "recurbill_comment"),
    path('recurbill_add_file/<id>',views.recurbill_add_file,name = "recurbill_add_file"),
   # path('recurbill_email/<id>', views.recurbill_email, name='recurbill_email'),
    path('get_comments/<str:profile_name>/', views.get_comments, name='get_comments'),
    path('every_terms',views.every_terms,name='every_terms'),
    
    path('cust_create',views.cust_create,name='cust_create'),
    path('customer_me',views.customer_me,name='customer_me'),
    
    path('recurbills_customer',views.recurbills_customer,name='recurbills_customer'),
    path('customer_dropdown',views.customer_dropdown,name = 'customer_dropdown'),
    
    path('payment_termA',views.payment_termA,name='payment_termA'),
    path('entr_custmrA', views.entr_custmrA, name='entr_custmrA'),
    
    path('dashboard',views.dashboard, name='dashboard'),
    
    path('view_customr', views.view_customr, name='view_customr'),
    path('view_one_customer/<int:id>', views.view_one_customer, name='view_one_customer'),
    path('view_customr_sname', views.view_customr_sname, name='view_customr_sname'),
    path('view_customr_scpname', views.view_customr_scpname, name='view_customr_scpname'),
   
    path('editcustomer/<int:id>', views.editcustomer, name='editcustomer'),
    path('editEnter_customer/<int:id>', views.editEnter_customer, name='editEnter_customer'),
    path('delete_customr/<int:id>', views.delete_customr, name='delete_customr'),
    path('add_email_customer', views.add_email_customer, name='add_email_customer'),
    path('sendmail', views.sendmail, name='sendmail'),
    
    path('paymentmethod',views.paymentmethod,name='paymentmethod'),
    path('paymentadd_method',views.paymentadd_method,name='paymentadd_method'),
    path('payment_add_details',views.payment_add_details,name='payment_add_details'),
    path('payment/<int:payment_id>', views.payment_details_view, name='payment_details'),
    path('payment_edit/<int:pk>',views.payment_edit,name='payment_edit'),
    path('payment_edit_view/<int:pk>',views.payment_edit_view,name='payment_edit_view'),
    
    path('purchaseView',views.purchaseView,name='purchaseView'),
  
    path('purchase_order',views.purchase_order,name='purchase_order'),
    path('purchase_vendor',views.purchase_vendor,name='purchase_vendor'),
    path('purchase_customer',views.purchase_customer,name='purchase_customer'),
    path('customer_dropdown',views.customer_dropdown,name='customer_dropdown'),
    path('payment_dropdown',views.payment_dropdown,name='payment_dropdown'),
    path('purchase_pay',views.purchase_pay,name='purchase_pay'),
    path('customer_det',views.customer_det,name='customer_det'),
    
    path('vendor_det',views.vendor_det,name='vendor_det'),
    path('create_Purchase_order',views.create_Purchase_order,name='create_Purchase_order'),
    path('purchase_unit',views.purchase_unit,name='purchase_unit'),
    path('purchase_unit_dropdown',views.purchase_unit_dropdown,name='purchase_unit_dropdown'),

    path('purchase_item',views.purchase_item,name='purchase_item'),
    path('purchase_item_dropdown',views.purchase_item_dropdown,name='purchase_item_dropdown'),

    path('purchase_account',views.purchase_account,name='purchase_account'),
    path('purchase_account_dropdown',views.purchase_account_dropdown,name='purchase_account_dropdown'),
    path('purchase_delet/<int:id>',views.purchase_delet,name='purchase_delet'),
    path('purchase_bill_view/<int:id>',views.purchase_bill_view,name='purchase_bill_view'),

    #path('EmailAttachementView_purchase', views.EmailAttachementView_purchase, name='EmailAttachementView_purchase'),
    path('export_purchase_pdf/<id>',views.export_purchase_pdf,name = "export_purchase_pdf"),
    
    path('edit/<int:pk>',views.edit,name='edit'),
    path('change_status/<int:pk>',views.change_status,name='change_status'),
    path('change_status_draft/<int:pk>',views.change_status_draft,name='change_status_draft'),
    path('draft/<int:id>',views.draft,name='draft'),
    path('Approved/<int:id>',views.Approved,name='Approved'),


    path('edit_Purchase_order/<int:id>',views.edit_Purchase_order,name='edit_Purchase_order'),
    
    # Chart Of account


    path('chartofaccount_home',views.chartofaccount_home,name='chartofaccount_home'),
    path('create_account',views.create_account,name='create_account'),
    path('chartofaccount_view/<int:id>',views.chartofaccount_view,name='chartofaccount_view'),
    path('create_account_view',views.create_account_view,name='create_account_view'),
    path('edit_chart_of_account/<int:pk>',views.edit_chart_of_account,name="edit_chart_of_account"),
    path('upload_chart_of_account/<int:pk>',views.upload_chart_of_account,name="upload_chart_of_account"),
    path('download_chart_of_account/<int:pk>',views.download_chart_of_account,name="download_chart_of_account"),
    
    path('proj', views.proj, name='proj'),
	path('vproj', views.vproj, name='vproj'),
	path('addproj', views.addproj, name='addproj'),
	path('overview/<int:id>/', views.overview, name='overview'),
	path('editproj/<int:id>',views.editproj,name='editproj'),
	path('editprojdb/<int:id>',views.editprojdb,name='editprojdb'),
	path('delproj/<int:id>',views.delproj,name='delproj'),
	path('createuser', views.createuser, name='createuser'),
	path('comment/<int:id>', views.comment, name='comment'),
	path('commentdb/<int:id>', views.commentdb, name='commentdb'),
	path('toggle-status/<int:project_id>/', views.toggle_status, name='toggle_status'),
	path('itemdata2', views.itemdata2, name='itemdata2'),
	
	path('comment', views.comment, name='comment'),
	path('commentdb/<int:id>',views.commentdb,name='commentdb'),
	
	path("drf",views.drf,name='drf'),
    path('apr',views.apr,name='apr'),
     
     path('report_inventory_view',views.report_inventory_view,name='report_inventory_view'),
     path('inventory_summary',views.inventory_summary,name='inventory_summary'),
     path('custom_repot',views.custom_repot,name='custom_repot'),

     path('inventory_Valuation_summary',views.inventory_Valuation_summary,name='inventory_Valuation_summary'),
     path('custom_valuation_repot',views.custom_valuation_repot,name='custom_valuation_repot'),
    path('show_hide',views.show_hide,name='show_hide'),
    path('general',views.general,name='general'),
    #------------------------------------------------------------------------------------------------sumayya---purchase bills
    path('view_bills',views.view_bills,name='view_bills'),
    path('new_bill/',views.new_bill,name='new_bill'),
    path('get_customer_data_bill/',views.get_customer_data_bill,name='get_customer_data_bill'),
    path('get_vendor_data_bill/',views.get_vendor_data_bill,name='get_vendor_data_bill'),
    path('create_purchase_bill/',views.create_purchase_bill,name='create_purchase_bill'),
    path('create_purchase_bill1/',views.create_purchase_bill1,name='create_purchase_bill1'),
    path('itemdata_bills/',views.itemdata_bills,name='itemdata_bills'),
    path('bill_view/<int:b_id>',views.bill_view,name='bill_view'),
    path('edit_bill/<int:bill_id>',views.edit_bill,name='edit_bill'),
    path('update_bills/<int:pk>',views.update_bills,name='update_bills'),
    path('add_comment_bills/<int:bill_id>',views.add_comment_bills,name='add_comment_bills'),
    path('upload_file_bills/<int:bill_id>',views.upload_file_bills,name='upload_file_bills'),
    path('delete_bill/<int:bill_id>',views.delete_bill,name='delete_bill'),
    path('search_bill/',views.search_bill,name='search_bill'),
    
    path('entr_custmr_for_bills/',views.entr_custmr_for_bills,name='entr_custmr_for_bills'),
    path('add_vendor_bills/',views.add_vendor_bills,name='add_vendor_bills'),
    path('additem_bills/',views.additem_bills,name='additem_bills'),
    path('create_account_bills/',views.create_account_bills,name='create_account_bills'),
    path('create_payment_terms_bills/',views.create_payment_terms_bills,name='create_payment_terms_bills'),
    #-------------------

    path('customerAtoZ_bills',views.customerAtoZ_bills,name='customerAtoZ_bills'),
    path('vendorAtoZ_bills',views.vendorAtoZ_bills,name='vendorAtoZ_bills'),
##gst report####
    path('gst_reports_gst2',views.gst_reports_gst2,name='gst_reports_gst2'),
    path('gstr2_load',views.gstr2_load,name='gstr2_load'),
    path('sales_by_hsn_load',views.sales_by_hsn_load,name="sales_by_hsn_load"),
  

    
    path('add_customers',views.add_customers,name='add_customers'),
    path('profileasc',views.profileasc,name='profileasc'),
    path('profiledesc',views.profiledesc,name='profiledesc'),
    
    path('payment_details_view/<int:pk>/', views.payment_details_view, name='payment_details_view'),
    path('payment_edit',views.payment_edit,name='payment_edit'),
    path('payment_lists/<int:payment_id>/', views.payment_lists, name='payment_lists'), 
    path('payment_template',views.payment_template,name='payment_template'), 
    path('payment/delete/<int:payment_id>',views.delete_payment,name='delete_payment'),
    path('payment_delete_details',views.payment_delete_details,name='payment_delete_details'),
	
    
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
    
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)