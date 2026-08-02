from flask import Flask, jsonify, request, Response
from prometheus_client import Counter, generate_latest

from database import db
from models import Order

app = Flask(__name__)

# PostgreSQL Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://enterprise_user:enterprise_password@localhost:5432/enterprise_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# Prometheus Counter
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP Requests"
)


@app.route("/")
def home():
    REQUEST_COUNT.inc()

    return jsonify({
        "service": "Order Service",
        "status": "Running"
    })


@app.route("/health")
def health():
    REQUEST_COUNT.inc()

    return jsonify({
        "status": "UP"
    })


# Get All Orders
@app.route("/orders", methods=["GET"])
def get_orders():
    REQUEST_COUNT.inc()

    orders = Order.query.all()

    return jsonify([order.to_dict() for order in orders])


# Create Order
@app.route("/orders", methods=["POST"])
def create_order():
    REQUEST_COUNT.inc()

    data = request.get_json()

    order = Order(
        symbol=data["symbol"],
        side=data["side"],
        quantity=data["quantity"],
        price=data["price"]
    )

    db.session.add(order)
    db.session.commit()

    return jsonify(order.to_dict()), 201


# Get Order By ID
@app.route("/orders/<int:order_id>", methods=["GET"])
def get_order(order_id):
    REQUEST_COUNT.inc()

    order = Order.query.get_or_404(order_id)

    return jsonify(order.to_dict())


# Delete Order
@app.route("/orders/<int:order_id>", methods=["DELETE"])
def delete_order(order_id):
    REQUEST_COUNT.inc()

    order = Order.query.get_or_404(order_id)

    db.session.delete(order)
    db.session.commit()

    return jsonify({
        "message": "Order deleted successfully"
    })


# Prometheus Metrics
@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype="text/plain"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)