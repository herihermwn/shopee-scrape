<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="Start your development with a Dashboard for Bootstrap 4.">
    <meta name="author" content="Creative Tim">

    <title>Argon - Shipping Cost</title>
    
    <!-- Favicon -->
    <link rel="icon" href="/static/img/brand/favicon.png" type="image/png">
    
    <!-- Fonts -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open+Sans:300,400,600,700">

    <!-- Icons -->
    <link rel="stylesheet" href="/static/vendor/nucleo/css/nucleo.css" type="text/css">
    <link rel="stylesheet" href="/static/vendor/@fortawesome/fontawesome-free/css/all.min.css" type="text/css">
    
    <!-- Page plugins -->
    
    <!-- Argon CSS -->
    <link rel="stylesheet" href="/static/css/argon.css" type="text/css">
</head>

<body>
    <!-- Sidenav -->
    <nav class="sidenav navbar navbar-vertical  fixed-left  navbar-expand-xs navbar-light bg-white" id="sidenav-main">
        <div class="scrollbar-inner">
            <!-- Brand -->
            <div class="sidenav-header  align-items-center">
                <a class="navbar-brand" href="javascript:void(0)">
                    <img src="/static/img/brand/blue.png" class="navbar-brand-img" alt="...">
                </a>
            </div>
            <div class="navbar-inner">
                <!-- Collapse -->
                <div class="collapse navbar-collapse" id="sidenav-collapse-main">
                    <!-- Nav items -->
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link" href="/">
                                <i class="ni ni-tv-2 text-primary"></i>
                                <span class="nav-link-text">Search Item</span>
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link active" href="/items">
                                <i class="ni ni-planet text-orange"></i>
                                <span class="nav-link-text">Item List</span>
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </nav>

    <!-- Main content -->
    <div class="main-content" id="panel">
        <!-- Header -->
        <div class="header bg-primary pb-6">
            <div class="container-fluid">
                <div class="header-body">
                    <div class="row align-items-center py-4">
                        <div class="col-lg-8">
                            <h6 class="h2 text-white d-inline-block mb-0">List Item</h6>
                            <nav aria-label="breadcrumb" class="d-none d-md-inline-block ml-md-4">
                                <ol class="breadcrumb breadcrumb-links breadcrumb-dark">
                                    <li class="breadcrumb-item"><a href="#"><i class="fas fa-home"></i></a></li>
                                    <li class="breadcrumb-item"><a href="#">Dashboards</a></li>
                                    <li class="breadcrumb-item active" aria-current="page">List Item</li>
                                </ol>
                            </nav>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Page content -->
        <div class="container-fluid mt--6">            
            <div class="row" id="shipping-summary">
                <div class="col-xl-12">
                    <div class="card">
                        <div class="card-header border-0 pb-0">
                            <div class="row align-items-center">
                                <div class="col">
                                    <h3 class="mb-0">Item List</h3>
                                </div>
                            </div>
                        </div>
                        <div class="card-body">
                            <div class="table-responsive">
                                <table witdh="100%" class="table table-striped" id="table-service">
                                    <thead class="thead-light">
                                        <tr>
                                            <th scope="col">Image</th>
                                            <th scope="col">Item ID</th>
                                            <th scope="col">Name</th>
                                            <th scope="col">Stock</th>
                                            <th scope="col">Brand</th>
                                            <th scope="col">Price</th>
                                            <th scope="col">Action</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        %for item in items:
                                            <tr>
                                                <td class="align-middle">
                                                    <image src="{{ item['item_photo_url'] }}" style="width: 50px; height: 50px; object-fit: cover">
                                                </td>
                                                <th class="align-middle" scope="row">{{ item['item_id'] }}</th>
                                                <td class="align-middle">
                                                    <a href="{{ item['item_detail_url'] }}" target="_blank">{{ item['item_name'] }}</a>
                                                </td>
                                                <td class="align-middle">{{ item['item_stock'] }}</td>
                                                <td class="align-middle">{{ item['item_brand'] }}</td>
                                                <td class="align-middle">{{ item['item_price'] }}</td>
                                                <td>
                                                    <form action="/items/{{ item['item_id'] }}/delete" method="POST">
                                                        <button class="btn btn-danger" type="submit">Delete Item</button>
                                                    </form>
                                                </td>
                                            </tr>
                                        %end
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Core -->
    <script src="static',filename='vendor/jquery/dist/jquery.min.js') }}"></script>
    <script src="static',filename='vendor/bootstrap/dist/js/bootstrap.bundle.min.js') }}"></script>
    <script src="static',filename='vendor/js-cookie/js.cookie.js') }}"></script>
    <script src="static',filename='vendor/jquery.scrollbar/jquery.scrollbar.min.js') }}"></script>
    <script src="static',filename='vendor/jquery-scroll-lock/dist/jquery-scrollLock.min.js') }}"></script>
    
    <!-- Argon JS -->
    <script src="static',filename='js/argon.js') }}"></script>

    <script>
        
    </script>
</body>

</html>