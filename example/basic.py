from gpdf import GpdfApi

API_KEY = "...."

# an api instance
gpdf_api = GpdfApi(API_KEY)

# send basic request
res = gpdf_api.send_request("example-slug")

print(res.get_url())

# send requests with variables
res = gpdf_api.send_request("another-slug", var_name="var_value")

res.save_pdf("/tmp/report.pdf")
