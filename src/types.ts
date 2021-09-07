export interface Product {
  id: number,
  name?: string,
  slogan?: string,
  description?: string,
  category?: string,
  default_price?: number,
  related: Array<number>,
  features?: []
}
