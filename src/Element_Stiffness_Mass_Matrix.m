function [K_el M_el] = Element_Stiffness_Mass_Matrix(t, p, el)
	x = p(:, 1); 
	y = p(:, 2);

	% Eckpunkte des Elements 
	p0 = [x(t(el, 1)); y(t(el, 1))]; 
	p1 = [x(t(el, 2)); y(t(el, 2))];
	p2 = [x(t(el, 3)); y(t(el, 3))];

	% Jacobian:
	J_el = [p1-p0 p2-p0];

	%J_el = [p(t(el,2),1)-p(t(el,1),1), p(t(el,3),1)-p(t(el,1),1) ; p(t(el,2),2)-p(t(el,1),2), p(t(el,3),2)-p(t(el,1),2)];

	area_el = 0.5 * abs(det(J_el));

	% Elementmassenmatrix:
	M_el = 2 * area_el * 1/24 * [2 1 1; 1 2 1; 1 1 2];

	H1 = [-1 -1; 1 0; 0 1];
	H2 = [-1 1 0; -1 0 1];
	J_el_inv = inv(J_el);
	K_el = area_el * H1 * J_el_inv * J_el_inv' * H2;
end
