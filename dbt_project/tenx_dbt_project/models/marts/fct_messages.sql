SELECT
  id,
  date,
  LENGTH(text) AS message_length,
  has_media,
  sender_id,
  channel
FROM {{ ref('stg_telegram_messages') }}
