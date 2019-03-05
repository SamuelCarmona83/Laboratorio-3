
CREATE SEQUENCE public.user_user_id_seq;

CREATE TABLE public.user (
                user_id INTEGER NOT NULL DEFAULT nextval('public.user_user_id_seq'),
                balance_amount REAL NOT NULL,
                name VARCHAR NOT NULL,
                shopcar_id VARCHAR NOT NULL,
                CONSTRAINT user_id PRIMARY KEY (user_id)
);


ALTER SEQUENCE public.user_user_id_seq OWNED BY public.user.user_id;

CREATE SEQUENCE public.shopping_car_shopcar_id_seq;

CREATE TABLE public.Shopping_car (
                shopcar_id VARCHAR NOT NULL DEFAULT nextval('public.shopping_car_shopcar_id_seq'),
                user_id INTEGER NOT NULL,
                products_id INTEGER NOT NULL,
                number INTEGER NOT NULL,
                CONSTRAINT shopcar_id PRIMARY KEY (shopcar_id)
);


ALTER SEQUENCE public.shopping_car_shopcar_id_seq OWNED BY public.Shopping_car.shopcar_id;

CREATE SEQUENCE public.product_table_product_id_seq;

CREATE TABLE public.product_table (
                product_id INTEGER NOT NULL DEFAULT nextval('public.product_table_product_id_seq'),
                shopcar_id VARCHAR NOT NULL,
                aviable_amount INTEGER DEFAULT 0 NOT NULL,
                price_peer_unit REAL NOT NULL,
                CONSTRAINT product_id PRIMARY KEY (product_id)
);


ALTER SEQUENCE public.product_table_product_id_seq OWNED BY public.product_table.product_id;

ALTER TABLE public.Shopping_car ADD CONSTRAINT user_shopping_car_fk
FOREIGN KEY (user_id)
REFERENCES public.user (user_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.product_table ADD CONSTRAINT shopping_car_product_table_fk
FOREIGN KEY (shopcar_id)
REFERENCES public.Shopping_car (shopcar_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;
