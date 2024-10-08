# Metric Forge

<img src="https://raw.githubusercontent.com/jrasband-dev/metric-forge/fb6a5ed63c35eda1443c3e6cedd9b4f4b18d5e41/static/metric-forge.svg" alt="Description of the image" width="300" height="300">

Metric Forge is your ultimate toolkit for measuring and evaluating performance across various business domains.

### Disclaimer

Metric Forge provides a collection of calculations across various domains, including finance, mortgage, marketing, and more. While every effort has been made to ensure the accuracy and reliability of the calculations and methods provided, Metric Forge is intended for informational and educational purposes only.

Important Notice:

No Warranty: The calculations and methods provided in this package are offered "as-is" without any guarantees or warranties of any kind, either express or implied. The package's creators do not assume any responsibility for errors or omissions or for any damages resulting from the use of the package.

Not Professional Advice: The results produced by the package should not be considered as professional financial, investment, legal, or any other type of advice. Users should consult with qualified professionals before making any decisions based on the outputs generated by this package.

Use at Your Own Risk: Users of Metric Forge assume full responsibility for the use of the package and its results. The creators of the package shall not be held liable for any decisions made based on the information provided or for any consequences arising from the use of the package.

By using this package, you acknowledge and agree to this disclaimer. If you do not agree, please refrain from using the Metric Forge package.


## Getting Started 
install the package via pip

```python
pip install metric-forge
```

## Ecommerce
You can use Ecommerce Metrics in two different ways:
* With Polars
* As a Single Value Function (SVF)

Metric Forge extends the Polars expression library; making it possible to perform row-wise-calculations for various metrics. In addition to mass calculations, you can also perform single value calculations that return just one value. 


```python
from metric_forge.ecommerce import * 
import polars as pl
data = pl.read_csv('datasets/ecommerce_metrics.csv')
data.head()
```




<div><style>
.dataframe > thead > tr,
.dataframe > tbody > tr {
  text-align: right;
  white-space: pre-wrap;
}
</style>
<small>shape: (5, 15)</small><table border="1" class="dataframe"><thead><tr><th>month</th><th>total_revenue</th><th>number_of_orders</th><th>cost_of_acquisition</th><th>new_customers</th><th>carts_created</th><th>completed_purchases</th><th>revenue_from_ads</th><th>advertising_spend</th><th>num_conversions</th><th>num_visitors</th><th>revenue_per_customer</th><th>average_customer_lifetime</th><th>num_customers_lost</th><th>total_customers_beginning</th></tr><tr><td>str</td><td>f64</td><td>i64</td><td>f64</td><td>i64</td><td>i64</td><td>i64</td><td>f64</td><td>f64</td><td>i64</td><td>i64</td><td>f64</td><td>f64</td><td>i64</td><td>i64</td></tr></thead><tbody><tr><td>&quot;2023-01&quot;</td><td>87454.011885</td><td>991</td><td>22958.350559</td><td>406</td><td>1969</td><td>1425</td><td>81339.957696</td><td>5390.910169</td><td>300</td><td>13154</td><td>202.427329</td><td>3.159364</td><td>239</td><td>3306</td></tr><tr><td>&quot;2023-02&quot;</td><td>145071.430641</td><td>913</td><td>18736.874206</td><td>234</td><td>1506</td><td>1421</td><td>76875.083402</td><td>15585.037018</td><td>427</td><td>14762</td><td>116.173436</td><td>1.812245</td><td>124</td><td>4680</td></tr><tr><td>&quot;2023-03&quot;</td><td>123199.394181</td><td>1305</td><td>28355.586842</td><td>120</td><td>1497</td><td>965</td><td>116505.482191</td><td>14872.037954</td><td>367</td><td>10056</td><td>384.265156</td><td>4.771414</td><td>177</td><td>4675</td></tr><tr><td>&quot;2023-04&quot;</td><td>109865.84842</td><td>885</td><td>14184.81582</td><td>428</td><td>1963</td><td>1102</td><td>106008.046381</td><td>12337.204368</td><td>132</td><td>19948</td><td>144.356328</td><td>3.395462</td><td>299</td><td>2972</td></tr><tr><td>&quot;2023-05&quot;</td><td>65601.864044</td><td>691</td><td>18764.339456</td><td>266</td><td>1009</td><td>801</td><td>97258.809912</td><td>5351.995568</td><td>147</td><td>13110</td><td>275.734601</td><td>3.77914</td><td>296</td><td>3768</td></tr></tbody></table></div>



#### Customer Acquisition Cost


```python
data.select(pl.col('cost_of_acquisition'),
            pl.col('new_customers'),
            pl.col('*').forge_ecommerce.customer_acquisition_cost('cost_of_acquisition', 'new_customers'))
```

#### Average Order Value


```python
data.select(pl.col('total_revenue'),
            pl.col('new_customers'),
            pl.col('*').forge_ecommerce.average_order_value('total_revenue', 'number_of_orders'))
```

#### Cart Abandonment Rate


```python
data.select(pl.col('carts_created'),
            pl.col('completed_purchases'),
            pl.col('*').forge_ecommerce.cart_abandonment_rate('carts_created', 'completed_purchases'))

```

#### Return on Advertising Spend


```python
data.select(pl.col('revenue_from_ads'),
            pl.col('advertising_spend'),
            pl.col('*').forge_ecommerce.return_on_advertising_spend('revenue_from_ads', 'advertising_spend'))
```

#### Conversion Rate


```python
data.select(pl.col('num_conversions'),
            pl.col('num_visitors'),
            pl.col('*').forge_ecommerce.conversion_rate('num_conversions', 'num_visitors'))
```

#### Customer Lifetime Value


```python
data.select(pl.col('revenue_per_customer'),
            pl.col('average_customer_lifetime'),
            pl.col('*').forge_ecommerce.customer_lifetime_value(revenue_per_customer_column='revenue_per_customer',average_customer_lifetime_column='average_customer_lifetime',method='basic'))
```




<div><style>
.dataframe > thead > tr,
.dataframe > tbody > tr {
  text-align: right;
  white-space: pre-wrap;
}
</style>
<small>shape: (12, 3)</small><table border="1" class="dataframe"><thead><tr><th>revenue_per_customer</th><th>average_customer_lifetime</th><th>customer_lifetime_value</th></tr><tr><td>f64</td><td>f64</td><td>f64</td></tr></thead><tbody><tr><td>202.427329</td><td>3.159364</td><td>639.54169</td></tr><tr><td>116.173436</td><td>1.812245</td><td>210.534716</td></tr><tr><td>384.265156</td><td>4.771414</td><td>1833.488253</td></tr><tr><td>144.356328</td><td>3.395462</td><td>490.156408</td></tr><tr><td>275.734601</td><td>3.77914</td><td>1042.039585</td></tr><tr><td>&hellip;</td><td>&hellip;</td><td>&hellip;</td></tr><tr><td>290.148089</td><td>2.182535</td><td>633.258286</td></tr><tr><td>325.310229</td><td>1.421977</td><td>462.583676</td></tr><tr><td>378.206435</td><td>2.826138</td><td>1068.863683</td></tr><tr><td>155.732582</td><td>1.873762</td><td>291.805755</td></tr><tr><td>341.766952</td><td>2.66604</td><td>911.164293</td></tr></tbody></table></div>
