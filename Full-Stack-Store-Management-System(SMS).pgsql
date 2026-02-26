Full-Stack-Store-Management-System(SMS)
│   
├── backend(with Python)
│   ├── app/
│   │   ├── __init__.py                          
│   │   ├── main.py                                           # FastAPI entry point
│   │   ├── core/                                             # App configuration & security
│   │   │   ├── config.py.py
│   │   │   ├── security.py
│   │   │   ├── dependencies.py
│   │   │   └── __init__.py
│   │   ├── db/                          
│   │   │   ├── base.py                                       # Base model
│   │   │   ├── session.py                                    # DB session
│   │   │   ├── init_db.py
│   │   │   └── __init__.py
│   │   ├── models/                                           # SQLAlchemy model
│   │   │   ├── user.py
│   │   │   ├── product.py
│   │   │   ├── category.py
│   │   │   ├── sale.py
│   │   │   ├── sale_item.py
│   │   │   ├── purchase.py
│   │   │   ├── purchase_item.py
│   │   │   ├── customer.py 
│   │   │   ├── supplier.py
│   │   │   └── __init__.py
│   │   ├── schemas/                                          # Pydantic schemas
│   │   │   ├── user.py
│   │   │   ├── auth.py
│   │   │   ├── product.py
│   │   │   ├── category.py
│   │   │   ├── sale.py
│   │   │   ├── purchase.py
│   │   │   ├── customer.py
│   │   │   ├── supplier.py
│   │   │   └── __init__.py
│   │   ├── repositories/                                    # DB Logic Layer (Optional but clean)
│   │   │   ├── user_repo.py
│   │   │   ├── auth_repo.py
│   │   │   ├── product_repo.py
│   │   │   ├── category_repo.py
│   │   │   ├── sale_repo.py
│   │   │   ├── purchase_repo.py
│   │   │   ├── customer_repo.py
│   │   │   ├── supplier_repo.py
│   │   │   └── __init__.py                          
│   │   ├── services/                                        # Business logic
│   │   │   ├── user_service.py
│   │   │   ├── auth_service.py
│   │   │   ├── product-service.py
│   │   │   ├── category_service.py
│   │   │   ├── sale_service.py
│   │   │   ├── purchase_service.py
│   │   │   ├── customer_service.py
│   │   │   ├── supplier_service.py
│   │   │   └── __init__.py
│   │   ├── api/                                             # Routes (instead of controllers + routes)
│   │   │   ├── deps.py
│   │   │   ├── auth.py
│   │   │   ├── products.py
│   │   │   ├── categories.py
│   │   │   ├── sales.py
│   │   │   ├── purchases.py
│   │   │   ├── customers.py
│   │   │   ├── suppliers.py
│   │   │   └── router.py                                    # Combines all routes
│   │   ├── middlewares/                          
│   │   │   ├── error_handler.py
│   │   │   └── auth.py
│   │   ├── utils/                          
│   │   │   ├── response.py
│   │   │   ├── validators.py
│   │   │   └── constants.py
│   │   ├── alembic/                          
│   │   ├── app.js                          
│   │   └── providers/
│   │       ├── test_auth.py
│   │       ├── test_product.py
│   │       └── test_order.js
│	├── alembic/                                             # Migrations (important for PostgreSQL)
│	├── tests/
│   │   ├── test_auth.py
│   │   ├── test_products.py
│   │   ├── test_sales.py
│   │   └── conftest.py
│	├── requirements.txt
│	├── .env
│	├── .gitignore
│   └── README.md 
│   
├── Frontend(SMS with React.js)
│   │
│   ├── public/
│   │   ├── index.html
│   │   └── favicon.ico
│   ├── src/
│   │   ├── assets/  
│   │	│	├── images/     
│   │	│	├── icon/                                     
│   │	│   └── styles/
│   │   │       ├── variables.css
│   │   │       ├── global.css
│   │   │   	└── theme.css
│   │   ├── components/                                            
│   │	│   ├── common/
│   │   │   │   ├── Button/
│   │   │   │   │   ├── Button.jsx
│   │   │   │	│   └── button.module.jsx
│   │   │   │   ├── Input/
│   │   │   │   │   ├── Input.jsx
│   │   │   │	│   └── Input.module.jsx
│   │   │   │   ├── Modal.jsx
│   │   │   │   ├── Table.jsx
│   │   │   │   ├── Card.jsx
│   │   │   │	└── Loader.jsx
│   │	│   ├── layout/
│   │   │   │   ├── Navbar.jsx
│   │   │   │   ├── Sidebar.jsx
│   │   │   │   ├── Footer.jsx
│   │   │   │	└── Breadcrumb.jsx
│   │	│   └── protected/
│   │   │       ├── ProtectedRoute.jsx
│   │   │   	└── RoleBaseRoute.jsx
│   │	│ 
│   │   ├── features/                                             
│   │	│	├── auth/
│   │   │   │   ├── pages/
│   │   │   │   │   ├── Login.jsx
│   │   │   │   │   ├── Register.jsx
│   │   │   │	│   └── ForgotPassword.jsx
│   │   │   │   ├── authSlice.js
│   │   │   │	└── auth.api.js
│   │	│   ├── dashboard/
│   │   │   │   ├── Dashboard.jsx
│   │   │   │	└── widgets/
│   │   │   │       ├── StatsCard.jsx
│   │   │   │	    └── SaleChart.jsx
│   │	│   ├── products/
│   │   │   │   ├── pages/
│   │   │   │   │   ├── ProductList.jsx
│   │   │   │   │   ├── AddProduct.jsx
│   │   │   │	│   └── EditProduct.jsx
│   │   │   │   ├── components/
│   │   │   │	│   └── ProductForm.jsx
│   │   │   │	└── product.api.js
│   │	│   ├── inventory/
│   │   │   │   ├── pages/
│   │   │   │   │   ├── InventoryDashboard.jsx
│   │   │   │   │   ├── Cart.jsx
│   │   │   │	│   └── PaymentModal.jsx
│   │   │   │   ├── components/
│   │   │   │   │   ├── UpdateStockModal.jsx
│   │   │   │   │   ├── LowStockAlert.jsx
│   │   │   │	│   └── SupplierSelector.jsx
│   │   │   │	└── inventory.api.js                                # All API calls for Inventory
│   │	│   ├── sales/
│   │   │   │   ├── pages/
│   │   │   │   │   ├── Billing.jsx
│   │   │   │	│   └── Invoice.jsx
│   │   │   │   ├── components
│   │   │   │   │   ├── Cart.jsx
│   │   │   │	│   └── PaymentModal.jsx
│   │   │   │	└── sales.api.js
│   │	│   ├── customers/
│   │   │   │   ├── pages/
│   │   │   │   │   ├── CustomerList.jsx
│   │   │   │   │   ├── AddCustomer.jsx 
│   │   │   │   │   ├── EditCustomer.jsx
│   │   │   │	│   └── CustomerDetails.jsx
│   │   │   │	└── customer.api.js
│   │	│   ├── suppliers/
│   │   │   │   ├── pages/
│   │   │   │   │   ├── SupplierList.jsx
│   │   │   │   │   ├── AddSupplier.jsx
│   │   │   │   │   ├── EditSupplier.jsx
│   │   │   │	│   └── SupplierDetails.jsx
│   │   │   │	└── supplier.api.js
│   │	│   └── reports/
│   │   │       ├── Dashboard.jsx
│   │   │       ├── SaleReport.jsx
│   │   │       ├── InventoryReport.jsx
│   │   │       ├── CustomerReport.jsx
│   │   │   	└── SupplierReport.jsx
│   │   ├── context/
│   │	│   ├── AuthContext.jsx                                                         
│   │	│   ├── inventoryContext.js                            # Context inventory State   
│   │	│   ├── NotificationContext.jsx                            
│   │   │   └── index.js    
│   │   ├── services/                                          # API call
│   │	│   ├── api.js                                         # Central Axios Instance
│   │	│   ├── authService.js                                
│   │	│   ├── productService.js                     
│   │	│   ├── saleService.js                         
│   │	│   ├── customerService.js
│   │	│   ├── supplierService.js
│   │	│   ├── staffService.js   
│   │   │   └── index.js                                       # Optional , export all service
│   │   ├── hooks/
│   │	│   ├── useAuth.js                                
│   │	│   ├── useFetch.js            
│   │	│   ├── useDebounce.js   
│   │	│   ├── useInventory.js                                # Helper function
│   │	│   ├── useForm.js                            
│   │   │   └── index.js           
│   │   ├── utils/
│   │	│   ├── constants.js                                              
│   │	│   ├── validators.js
│   │	│   ├── inventoryHelper.js
│   │   │   └── helper.js  
│   │   ├── routes/
│   │	│   ├── AppRoutes.jsx
│   │   │   └── RouteConfig.jsx
│   │   ├── App.jsx                                   
│   │   └── main.jsx                                           
│   │   
│   └── data/                     
│       ├── 
│       └── 
├── static/                                     
│   └──    
├── .gitignore 
└── README.md
