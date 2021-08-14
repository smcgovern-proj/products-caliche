import express from 'express'
import db from './db'

const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('hello world!')
})

app.get('/products', (req, res) => {
  // db.get();
})
app.get('/products:product_id', (req, res) => {})
app.get('/products:product_id/styles', (req, res) => {})
app.get('/products:product_id/related', (req, res) => {})

app.listen(port, () => {
  console.log(`server listening on port ${port}`)
  console.log(db.readyState)
})

export default app
