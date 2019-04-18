


(define-macro (def func bindings body)
  `(define ,func (lambda ,bindings ,body))
  )


(define-macro (or-macro expr1 expr2)
    `(let ((v1 ,expr1))
        (if v1 v1 ,expr2)))

(define (flatmap f x)
  (begin (define (helper f x last)
	   (if (null? x) last
	       (helper f (cdr x) (append last (f (car x))))))
	 (helper f x nil)))

(define (expand lst)
  (begin (define (helper lst last)
	   (begin (cond ((null? lst) last)
			((eq? (car lst) 'x) (helper (cdr lst) (append last '(x r y f r))))
			((eq? (car lst) 'y) (helper (cdr lst) (append last '(l f x l y))))
			(else (helper (cdr lst) (append last `(,(car lst))))))))
	 (helper lst nil)))

(define (interpret instr dist)
  (begin (cond ((eq? instr 'f) (begin (fd dist) (print 'fd)))
	       ((eq? instr 'l) (lt dist) (print 'lt))
	       ((eq? instr 'r) (rt dist) (print 'rt)))))

(define (apply-many n f x)
  (if (zero? n)
      x
      (apply-many (- n 1) f (f x))))

(define (dragon n d)
  (interpret (apply-many n expand '(f x)) d))
