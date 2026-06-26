import pandas as pd

base_path = '../dados/'

df_orders = pd.read_csv(base_path + 'olist_orders_dataset.csv')
df_items = pd.read_csv(base_path + 'olist_order_items_dataset.csv')
df_payments = pd.read_csv(base_path + 'olist_order_payments_dataset.csv')
df_clientes = pd.read_csv(base_path + 'olist_customers_dataset.csv')

df_fato = pd.merge(df_items, df_orders, on='order_id', how='inner')
df_fato = pd.merge(df_fato, df_payments, on='order_id', how='left')
df_fato = df_fato.merge(df_clientes[['customer_id', 'customer_unique_id']], on='customer_id', how='left')

df_fato['price'] = df_fato['price'].fillna(0.0)
df_fato['freight_value'] = df_fato['freight_value'].fillna(0.0)
df_fato['payment_value'] = df_fato['payment_value'].fillna(0.0)

colunas_finais = [
    'order_id', 
    'customer_id',
    'seller_id', 
    'product_id', 
    "order_status",
    "customer_unique_id",
    'price', 
    'freight_value', 
    'payment_type',
    'payment_value',
    'payment_sequential',
    'payment_installments',
    'order_purchase_timestamp', 
    'order_approved_at',
    'order_delivered_carrier_date', 
    'order_delivered_customer_date',
    'order_estimated_delivery_date', 
    'shipping_limit_date'
]

colunas_de_data = [
    'order_purchase_timestamp', 
    'order_approved_at', 
    'order_delivered_carrier_date', 
    'order_delivered_customer_date', 
    'order_estimated_delivery_date',
    'shipping_limit_date'
]

df_fato = df_fato[colunas_finais]
for col in colunas_de_data:
    df_fato[col] = pd.to_datetime(df_fato[col]).dt.strftime('%Y-%m-%d 00:00:00.000')

caminho_saida = '../dados/fato_pronta_para_banco.csv'
df_fato.to_csv(caminho_saida, index=False)