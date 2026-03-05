$texts = @(
"Chennai summer is hotter than my production server",
"Anna Salai traffic has better load balancing than my app",
"Ranganathan Street is high throughput architecture",
"Chennai rains test disaster recovery every year",
"Spin bowling works well in Chennai conditions",
"Embeddings are just emotional numbers",
"The most awesome folks in Chennai today are the ones sitting in this AWS Community Day event"
)

foreach ($t in $texts) {
  s3vectors-embed put `
    --vector-bucket-name acd-chennai-s3-app-demo `
    --index-name s3-app-index `
    --model-id amazon.titan-embed-text-v2:0 `
    --text-value "$t"
}