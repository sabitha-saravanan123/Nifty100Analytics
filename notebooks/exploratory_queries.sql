SELECT COUNT(*) FROM companies;
SELECT COUNT(*) FROM profitandloss;
SELECT COUNT(*) FROM balancesheet;
SELECT COUNT(*) FROM cashflow;
SELECT MIN(year), MAX(year) FROM profitandloss;
SELECT company_id,COUNT(*) AS years_available FROM profitandloss GROUP BY company_id ORDER BY years_available;
SELECT company_id,COUNT(*) AS years_available FROM profitandloss GROUP BY company_id HAVING COUNT(*) < 5;