const express = require('express');
const jwt = require('jsonwebtoken');
const cors = require('cors');

const app = express();
app.use(express.json());
app.use(cors()); 

const SECRET_KEY = 'your_secret_key'; 


app.post('/api/login', (req, res) => {
    const { username, password } = req.body;

    
    if (username === 'user' && password === 'password') {
        const token = jwt.sign({ userId: 1, role: 'user' }, SECRET_KEY, { expiresIn: '1h' });
        return res.json({ token });
    }

    return res.status(401).json({ error: 'Неверные учетные данные' });
});


function authenticateToken(req, res, next) {
    const authHeader = req.headers['authorization'];
    const token = authHeader && authHeader.split(' ')[1];

    if (!token) return res.status(401).json({ error: 'Токен отсутствует' });

    jwt.verify(token, SECRET_KEY, (err, user) => {
        if (err) return res.status(403).json({ error: 'Неверный токен' });
        req.user = user;
        next();
    });
}


app.get('/api/protected', authenticateToken, (req, res) => {
    res.json({ message: 'Доступ разрешён!', user: req.user });
});


const PORT = 3000;
app.listen(PORT, () => console.log(`Сервер запущен на http://localhost:${PORT}`));
