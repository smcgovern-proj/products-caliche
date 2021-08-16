import express from 'express'
import db from './db'

const app = express()
const port = 3000

app.get('/', async (req, res) => {
  try {
    const response = await db.model('Product').findOne({})
    res.status(200).send(response)
  } catch (err) {
    res.status(500).send('err with db')
  }
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
