# 🚀 Déploiement d'une API Flask avec Kubernetes

Ce projet démontre comment déployer une API Flask avec une base de données PostgreSQL sur Kubernetes en utilisant ConfigMap et Secret pour la configuration.

## 📁 Structure du projet

```
flask-api/
│── app.py               # API Flask
│── requirements.txt     # Dépendances Python
│── Dockerfile           # Image Docker
│── k8s/                 # Déploiements Kubernetes
│   ├── deployment.yaml  # Déploiement et Service Flask
│   ├── service.yaml     # Service Flask
│   ├── postgres.yaml    # Déploiement PostgreSQL
│   ├── configmap.yaml   # ConfigMap pour la BD
│   ├── secret.yaml      # Secret pour les identifiants
```

---

## 🛠️ Installation et Déploiement

### 1️⃣ Cloner le projet
```bash
git clone https://github.com/Talla-hub/kubernetes-practice-projects.git
cd kubernetes-practice-projects/flask-api
```

### 2️⃣ Construire et pousser l'image Docker
```bash
docker build -t talla231hub/flask-api .
docker push talla231hub/flask-api
```

### 3️⃣ Déployer PostgreSQL et l’API Flask
```bash
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/secret.yaml
kubectl apply -f k8s/postgres.yaml
kubectl apply -f k8s/deployment.yaml
```

### 4️⃣ Vérifier les déploiements
```bash
kubectl get pods
kubectl get services
```

### 5️⃣ Tester l'application
```bash
minikube service flask-service --url
curl http://<minikube-ip>:<nodePort>
```

---

## 🔧 Configuration avec ConfigMap et Secret

### 📌 `configmap.yaml`
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: flask-config
data:
  db_host: "postgres-service"
  db_name: "mydatabase"
```

### 🔒 `secret.yaml`
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: flask-secret
type: Opaque
data:
  db_user: dXNlcg==   # Base64 de "user"
  db_password: cGFzc3dvcmQ=  # Base64 de "password"
```

Pour générer les valeurs :
```bash
echo -n "user" | base64
echo -n "password" | base64
```


