describe('jest install', () => {
  it('should run', () => {
      console.log('jest here')
    })
  }
)

describe('products endpoint', () => {
  it('should respond with status 500 if db errors', () => {})
  it('should respond with status 200 for valid GET request', () => {})
  it('should respond with data in correct shape', () => {})
})

describe('products/:product_id endpoint', () => {
  it('should respond with status 404 if id invalid', () => {})
  it('should respond with status 200 for valid id', () => {})
  it('should respond with data in correct shape', () => {})
})