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
                            <a class="nav-link active" href="/">
                                <i class="ni ni-tv-2 text-primary"></i>
                                <span class="nav-link-text">Search Item</span>
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/items">
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
                            <h6 class="h2 text-white d-inline-block mb-0">Search Item</h6>
                            <nav aria-label="breadcrumb" class="d-none d-md-inline-block ml-md-4">
                                <ol class="breadcrumb breadcrumb-links breadcrumb-dark">
                                    <li class="breadcrumb-item"><a href="#"><i class="fas fa-home"></i></a></li>
                                    <li class="breadcrumb-item"><a href="#">Dashboards</a></li>
                                    <li class="breadcrumb-item active" aria-current="page">Search Item</li>
                                </ol>
                            </nav>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Page content -->
        <div class="container-fluid mt--6">            
            <div class="row">
                <div class="col-xl-12">
                    <div class="card">
                        <div class="card-header border-0 pb-0">
                            <div class="row align-items-center">
                                <div class="col">
                                    <h3 class="mb-0">Search Item by Name</h3>
                                </div>
                            </div>
                        </div>
                        <div class="card-body">
                            <div class="row">
                                <div class="col-lg-12">
                                    <div class="alert d-none" id="alert-message" role="alert"></div>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-lg-9">
                                    <div class="form-group">
                                        <label class="form-control-label">Name</label>
                                        <input type="text" name="q" id="q" class="form-control" placeholder="Input the keyword here" required>
                                    </div>
                                </div>
                                <div class="col-lg-3">
                                    <div class="form-group">
                                        <label class="form-control-label">&nbsp;</label>
                                        <button class="btn btn-primary form-control" id="btn-submit">Submit</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row d-none" id="search-summary">
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
                                    <tbody></tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Core -->
    <script src="/static/vendor/jquery/dist/jquery.min.js"></script>
    <script src="/static/vendor/bootstrap/dist/js/bootstrap.bundle.min.js"></script>
    <script src="/static/vendor/js-cookie/js.cookie.js"></script>
    <script src="/static/vendor/jquery.scrollbar/jquery.scrollbar.min.js"></script>
    <script src="/static/vendor/jquery-scroll-lock/dist/jquery-scrollLock.min.js"></script>
    
    <!-- Argon JS -->
    <script src="/static/js/argon.js"></script>

    <script>
        function formatRupiah(angka, prefix){
			var number_string = angka.toString(),
			split   		= number_string.split(','),
			sisa     		= split[0].length % 3,
			rupiah     		= split[0].substr(0, sisa),
			ribuan     		= split[0].substr(sisa).match(/\d{3}/gi);
 
			// tambahkan titik jika yang di input sudah menjadi angka ribuan
			if(ribuan){
				separator = sisa ? '.' : '';
				rupiah += separator + ribuan.join('.');
			}
 
			rupiah = split[1] != undefined ? rupiah + ',' + split[1] : rupiah;
			return prefix == undefined ? rupiah : (rupiah ? 'Rp. ' + rupiah : '');
		}

        $(function () {
            $('#btn-submit').click(function () {
                let q = $('#q').val()

                $.ajax({
                    url: "/runspider",
                    type: 'POST',
                    dataType: 'json',
                    data: {
                        keyword: q
                    }
                }).done(function (res) {
                    var result = res.data
                    var dataLength = result.length
                    var row = null

                    if (dataLength > 0) {
                        for (i = 0; i < dataLength; i++) {
                            row += `<tr data-id="${result[i].item_id}">`
                            row += `<td class="align-middle"><image src="${result[i].item_photo_url}" style="width: 50px; height: 50px; object-fit: cover"></td>`
                            row += `<th class="align-middle" scope="row">${result[i].item_id}</th>`
                            row += `<td class="align-middle"><a href="${result[i].item_detail_url}" target="_blank">${result[i].item_name}</a></td>`
                            row += `<td class="align-middle">${result[i].item_stock}</td>`
                            row += `<td class="align-middle">${result[i].item_brand ?? 'None'}</td>`
                            row += `<td class="align-middle">${formatRupiah(result[i].item_price, 'Rp. ')}</td>`
                            row += `<td>
                                <form method="POST" action="/items/create">
                                    <input type="hidden" name="item_photo_url" value="${result[i].item_photo_url}">
                                    <input type="hidden" name="item_id" value="${result[i].item_id}">
                                    <input type="hidden" name="item_name" value="${result[i].item_name}">
                                    <input type="hidden" name="item_detail_url" value="${result[i].item_detail_url}">
                                    <input type="hidden" name="item_stock" value="${result[i].item_stock}">
                                    <input type="hidden" name="item_brand" value="${result[i].item_brand ?? 'None'}">
                                    <input type="hidden" name="item_price" value="${formatRupiah(result[i].item_price, 'Rp. ')}">
                                    <button class="btn btn-primary">Save Item</button>
                                </form>
                            </td>`
                            row += '</tr>'
                        }
                    }

                    $('#table-service tbody').html(row)
                    $('#search-summary').removeClass('d-none')
                }).fail(function (error) {
                    console.log(error)
                })
            })
        })
    </script>
</body>

</html>