SELECT 'Store Number'
FROM transactions left join stores on stores.'Store Number' = transaction.'Store Number'
;