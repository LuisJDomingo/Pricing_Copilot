def importe_total_carro(request):
    total = 0
    if request.user.is_authenticated and "carro" in request.session:
        for key, value in request.session["carro"].items():
            total += float(value["precio"]) * int(value["cantidad"])
    else:
        total="necesitas loguearte para comprar"
        
        
    return {"importe_total_carro": total}